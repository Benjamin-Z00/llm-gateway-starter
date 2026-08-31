import json
import time
from collections.abc import AsyncIterator

from fastapi import HTTPException
from jsonschema import ValidationError, validate

from app.models import ChatRequest, ChatResponse, StructuredRequest, StructuredResponse
from app.providers.base import ModelProvider
from app.services.tokenizer import estimate_messages_tokens, estimate_tokens
from app.services.usage import UsageStore


class LLMGateway:
    def __init__(self, provider: ModelProvider, usage_store: UsageStore) -> None:
        self.provider = provider
        self.usage_store = usage_store

    async def chat(self, request: ChatRequest) -> ChatResponse:
        started = time.perf_counter()
        content = await self.provider.complete(request)
        return self._build_chat_response(request, content, started)

    async def structured(self, request: StructuredRequest) -> StructuredResponse:
        started = time.perf_counter()
        last_error = "unknown validation error"

        for attempt in range(request.max_retries + 1):
            content = await self.provider.complete(request)
            try:
                data = json.loads(content)
                validate(instance=data, schema=request.schema_)
                input_tokens = estimate_messages_tokens(request.messages)
                output_tokens = estimate_tokens(content)
                cost = self._estimate_cost_cny(input_tokens, output_tokens)
                self.usage_store.record(input_tokens, output_tokens, cost)
                return StructuredResponse(
                    model=request.model,
                    data=data,
                    retries=attempt,
                    input_tokens=input_tokens,
                    output_tokens=output_tokens,
                    latency_ms=self._latency_ms(started),
                    cost_cny=cost,
                )
            except (json.JSONDecodeError, ValidationError) as exc:
                last_error = str(exc)

        raise HTTPException(
            status_code=422,
            detail=f"Model response did not match schema after retries: {last_error}",
        )

    async def stream_chat(self, request: ChatRequest) -> AsyncIterator[str]:
        input_tokens = estimate_messages_tokens(request.messages)
        output_text = ""
        async for chunk in self.provider.stream(request):
            output_text += chunk
            yield chunk

        output_tokens = estimate_tokens(output_text)
        cost = self._estimate_cost_cny(input_tokens, output_tokens)
        self.usage_store.record(input_tokens, output_tokens, cost)

    def _build_chat_response(
        self,
        request: ChatRequest,
        content: str,
        started: float,
    ) -> ChatResponse:
        input_tokens = estimate_messages_tokens(request.messages)
        output_tokens = estimate_tokens(content)
        cost = self._estimate_cost_cny(input_tokens, output_tokens)
        self.usage_store.record(input_tokens, output_tokens, cost)
        return ChatResponse(
            model=request.model,
            content=content,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=self._latency_ms(started),
            cost_cny=cost,
        )

    def _estimate_cost_cny(self, input_tokens: int, output_tokens: int) -> float:
        input_cost = input_tokens / 1000 * 0.001
        output_cost = output_tokens / 1000 * 0.002
        return round(input_cost + output_cost, 6)

    def _latency_ms(self, started: float) -> int:
        return int((time.perf_counter() - started) * 1000)
