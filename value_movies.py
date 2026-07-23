from movievalue.service import MovieValueService

from argparse import ArgumentParser
from pathlib import Path

from colorama import Fore, Style, init
from tqdm import tqdm

from movievalue.models import Movie
from movievalue.csv_io import MovieCSV
from movievalue.logger import logger

init(autoreset=True)


def parse_args():

    parser = ArgumentParser(
        description="Movie Collection Valuation Tool"
    )

    parser.add_argument(
        "csv_file",
        help="Input CSV file",
    )

    return parser.parse_args()


def main():

    args = parse_args()

    print(Fore.CYAN)
    print("=" * 60)
    print("Movie Collection Valuation Tool")
    print("=" * 60)
    print(Style.RESET_ALL)

    csv = MovieCSV(args.csv_file)

    logger.info("Loading CSV %s", args.csv_file)

    df = csv.load()

    print(f"Loaded {len(df)} movies")

    df = csv.add_output_columns(df)
    service = MovieValueService()

    #
    # Fake processing for now
    #
    for index, row in tqdm(
        df.iterrows(),
        total=len(df),
        desc="Valuing"):

        movie = Movie.from_series(row)

        logger.info("Looking up: %s", movie.title)

        valuation = service.value_movie(movie)

        csv.update_valuation(df, index, valuation)

    output = (
        Path("output")
        / f"{Path(args.csv_file).stem}_valued.csv"
    )

    csv.save(df, output)

    logger.info("Saved %s", output)

    print()
    print(Fore.GREEN + f"Finished!")
    print(f"Output written to {output}")


if __name__ == "__main__":
    main()