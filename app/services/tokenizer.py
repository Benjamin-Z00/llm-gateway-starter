def estimate_tokens(text: str) -> int:
    """Small deterministic token estimate for learning and cost accounting."""
    if not text.strip():
        return 0
    return max(1, len(text) // 4)


def estimate_messages_tokens(messages: list[object]) -> int:
    total = 0
    for message in messages:
        content = getattr(message, "content", "")
        total += estimate_tokens(content)
    return total
