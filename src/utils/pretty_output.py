from rich.console import Console
from rich.table import Table
from thoughtful_ai.dispatch import Dispatch


def rich_print(
    result: Dispatch | None, width: float, height: float, length: float, mass: float
) -> None:
    table = Table(title="Package Sorting Results")

    table.add_column("Attribute", style="cyan", justify="right")
    table.add_column("Value", style="magenta", justify="center")

    table.add_row("Width", str(width))
    table.add_row("Length", str(length))
    table.add_row("Height", str(height))
    table.add_row("Mass", str(mass))
    table.add_row("Sort Result", str(result))

    console = Console()
    console.print(table)
