from pathlib import Path

import pandas as pd


from movievalue.config import OUTPUT_COLUMNS


class MovieCSV:

    def __init__(self, filename):
        self.filename = Path(filename)

    def load(self):

        if not self.filename.exists():
            raise FileNotFoundError(self.filename)

        df = pd.read_csv(self.filename)

        required = [
            "Title",
            "Running Time",
            "Genre",
            "Director",
            "Barcode",
            "Format",
        ]

        missing = [c for c in required if c not in df.columns]

        if missing:
            raise ValueError(f"Missing columns: {missing}")

        return df

    def add_output_columns(self, df):

        for col in OUTPUT_COLUMNS:
            if col not in df.columns:
                df[col] = ""

        return df

    def save(self, df, output_filename):

        output = Path(output_filename)

        output.parent.mkdir(parents=True, exist_ok=True)

        df.to_csv(output, index=False)

        return output