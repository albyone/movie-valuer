from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

ROOT_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = ROOT_DIR / "output"
CACHE_DIR = ROOT_DIR / "cache"
LOG_DIR = ROOT_DIR / "logs"

OMDB_API_KEY = os.getenv("OMDB_API_KEY")
EBAY_CLIENT_ID = os.getenv("EBAY_CLIENT_ID")
EBAY_CLIENT_SECRET = os.getenv("EBAY_CLIENT_SECRET")

OUTPUT_COLUMNS = {
    "Estimated Value (AUD)": "float",
    "Confidence": "string",
    "Source": "string",
    "Notes": "string",
    "Last Checked": "string",
}