from dataclasses import dataclass
import pandas as pd


@dataclass
class Movie:
    title: str
    running_time: str
    genre: str
    director: str
    barcode: str
    format: str
    condition: str

    estimated_value: float
    confidence: str = ""
    source: str = ""
    notes: str = ""
    last_checked: str = ""

    @classmethod
    def from_series(cls, row: pd.Series):
        barcode = ""
        if pd.notna(row["Barcode"]):
            barcode = str(row["Barcode"]).replace(".0", "")
        return cls(
            title=str(row["Title"]).strip(),
            running_time=str(row["Running Time"]).strip(),
            genre=str(row["Genre"]).strip(),
            director=str(row["Director"]).strip(),
            barcode=barcode,
            format=str(row["Format"]).strip(),
            condition=str(row["Condition"]).strip(),
            estimated_value=row["Estimated Value (AUD)"],
            confidence=row["Confidence"],
            source=row["Source"],
            notes=str(row["Notes"]),
            last_checked=row["Last Checked"],
        )

@dataclass(slots=True)
class EbayListing:
    title: str
    condition: str
    price: float
    shipping: float