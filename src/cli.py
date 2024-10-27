import argparse

from thoughtful_ai.main import sort
from thoughtful_ai.dispatch import Dispatch
from utils.pretty_output import rich_print


def run() -> None:
    parser = argparse.ArgumentParser(
        description="Sort packages based on dimension and mass."
    )

    parser.add_argument("width", type=float, help="Width of the package in cm")
    parser.add_argument("length", type=float, help="Length of the package in cm")
    parser.add_argument("height", type=float, help="Height of the package in cm")
    parser.add_argument("mass", type=float, help="Mass of the package in cm")

    args: argparse.Namespace = parser.parse_args()

    result: Dispatch | None = sort(args.width, args.height, args.length, args.mass)
    rich_print(result, args.width, args.length, args.height, args.mass)
