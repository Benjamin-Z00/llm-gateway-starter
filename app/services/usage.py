from dataclasses import dataclass


@dataclass
class UsageStore:
    request_count: int = 0
    input_tokens: int = 0
    output_tokens: int = 0
    total_cost_cny: float = 0.0

    def record(self, input_tokens: int, output_tokens: int, cost_cny: float) -> None:
        self.request_count += 1
        self.input_tokens += input_tokens
        self.output_tokens += output_tokens
        self.total_cost_cny += cost_cny

    def snapshot(self) -> dict[str, int | float]:
        return {
            "request_count": self.request_count,
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "total_cost_cny": round(self.total_cost_cny, 6),
        }
