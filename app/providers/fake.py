import asyncio
import json
from collections.abc import AsyncIterator

from app.models import ChatRequest


class FakeModelProvider:
    """Deterministic local provider for tests and first-time learners."""

    async def complete(self, request: ChatRequest) -> str:
        last_user_message = next(
            (message.content for message in reversed(request.messages) if message.role == "user"),
            "",
        )

        if "return_invalid_json" in last_user_message:
            return "not-json"

        if "extract_profile" in last_user_message:
            return json.dumps(
                {
                    "name": "Alex",
                    "role": "backend engineer",
                    "goal": "learn AI Agent engineering",
                },
                ensure_ascii=False,
            )

        return f"Gateway response: {last_user_message}"

    async def stream(self, request: ChatRequest) -> AsyncIterator[str]:
        content = await self.complete(request)
        for word in content.split(" "):
            await asyncio.sleep(0)
            yield word
