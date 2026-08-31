from collections.abc import AsyncIterator
from typing import Protocol

from app.models import ChatRequest


class ModelProvider(Protocol):
    async def complete(self, request: ChatRequest) -> str:
        """Return a full model response."""

    async def stream(self, request: ChatRequest) -> AsyncIterator[str]:
        """Yield response chunks."""
