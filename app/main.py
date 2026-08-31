from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from app.models import ChatRequest, StructuredRequest
from app.providers.fake import FakeModelProvider
from app.services.gateway import LLMGateway
from app.services.usage import UsageStore

usage_store = UsageStore()
provider = FakeModelProvider()
gateway = LLMGateway(provider=provider, usage_store=usage_store)

app = FastAPI(
    title="LLM Gateway Starter",
    description="A small production-minded LLM Gateway for AI Agent engineering practice.",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/v1/chat")
async def chat(request: ChatRequest):
    return await gateway.chat(request)


@app.post("/v1/structured")
async def structured(request: StructuredRequest):
    return await gateway.structured(request)


@app.post("/v1/chat/stream")
async def stream_chat(request: ChatRequest):
    async def events():
        async for chunk in gateway.stream_chat(request):
            yield f"data: {chunk}\n\n"

    return StreamingResponse(events(), media_type="text/event-stream")


@app.get("/v1/usage")
def usage():
    return usage_store.snapshot()
