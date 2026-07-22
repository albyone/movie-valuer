from dataclasses import dataclass


@dataclass
class Movie:
    title: str
    running_time: str
    genre: str
    director: str
    barcode: str
    format: str

    estimated_value: float
    confidence: str = ""
    source: str = ""
    notes: str = ""
    last_checked: str = ""