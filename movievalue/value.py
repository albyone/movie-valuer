from dataclasses import dataclass


@dataclass
class MovieValue:
    value: float | None
    confidence: str
    source: str
    notes: str