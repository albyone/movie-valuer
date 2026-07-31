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
            "Condition",
        ]

        missing = [c for c in required if c not in df.columns]

        if missing:
            raise ValueError(f"Missing columns: {missing}")

        df = self.add_output_columns(df)

        return df

    def add_output_columns(self, df):

        for column, dtype in OUTPUT_COLUMNS.items():

            if column not in df.columns:
                df[column] = pd.Series(dtype=dtype)

        return df

    def save(self, df, output_filename):

        output = Path(output_filename)

        output.parent.mkdir(parents=True, exist_ok=True)

        df.to_csv(output, index=False)

        return output
    
    def update_valuation(self, df, index, valuation):

        df.at[index, "Estimated Value (AUD)"] = valuation.value
        df.at[index, "Confidence"] = valuation.confidence
        df.at[index, "Source"] = valuation.source
        df.at[index, "Notes"] = valuation.notes