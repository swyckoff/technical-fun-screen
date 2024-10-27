from utils.pretty_output import rich_print
import rich

from thoughtful_ai.main import sort
from thoughtful_ai.dispatch import Dispatch

rich.print(
    "[bold yellow]The [bold green]Run[/bold green] button uses hardcoded values. Try using the replit Shell with [bold blue]poetry run sort 1 2 3 4[/bold blue] to try other values."
)
width, height, length, mass = 1, 2, 3, 4
result: Dispatch | None = sort(width, height, length, mass)
rich_print(result, width, height, length, mass)
