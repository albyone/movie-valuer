import logging
from pathlib import Path

from movievalue.config import LOG_DIR

LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "movie-value.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

logger = logging.getLogger("movie-value")