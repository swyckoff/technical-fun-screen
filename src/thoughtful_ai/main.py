from typing import Union
from pydantic import ValidationError
from thoughtful_ai.dispatch import Dispatch
from thoughtful_ai.package import Package


def sort(
    width: float, height: float, length: float, mass: float
) -> Union[Dispatch, None]:
    """Helper function to determine the dispatch stack for a package based on the dimensions and mass.

    I use Enums instead of strings for the output to simplify refactoring, IDE autocompletion, limit the
    location of typos (very DRY), and it feels more readable.

    Returns:
        Dispatch (str): The name of the dispatch stack ('STANDARD', 'SPECIAL', 'REJECTED').
    """
    try:
        package = Package(width, height, length, mass)
        return package.sort()
    except ValidationError as ve:
        print(f"Invalid input: {ve.errors()[0]['msg']}")
    return None
