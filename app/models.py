from typing import Any, Literal

from pydantic import BaseModel, Field


Role = Literal["system", "user", "assistant"]


class Message(BaseModel):
    role: Role
    content: str = Field(min_length=1)


class ChatRequest(BaseModel):
    messages: list[Message] = Field(min_length=1)
    model: str = "fake-fast"
    temperature: float = Field(default=0.2, ge=0, le=2)
    max_tokens: int = Field(default=512, ge=1, le=4096)


class ChatResponse(BaseModel):
    model: str
    content: str
    input_tokens: int
    output_tokens: int
    latency_ms: int
    cost_cny: float


class StructuredRequest(ChatRequest):
    schema_: dict[str, Any] = Field(alias="schema")
    max_retries: int = Field(default=2, ge=0, le=5)


class StructuredResponse(BaseModel):
    model: str
    data: dict[str, Any]
    retries: int
    input_tokens: int
    output_tokens: int
    latency_ms: int
    cost_cny: float


class UsageSnapshot(BaseModel):
    request_count: int
    input_tokens: int
    output_tokens: int
    total_cost_cny: float
