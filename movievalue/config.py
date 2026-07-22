from pathlib import Path

OUTPUT_COLUMNS = {
    "Estimated Value (AUD)": "float",
    "Confidence": "string",
    "Source": "string",
    "Notes": "string",
    "Last Checked": "string",
}

OUTPUT_DIR = Path("output")
CACHE_DIR = Path("cache")
LOG_DIR = Path("logs")