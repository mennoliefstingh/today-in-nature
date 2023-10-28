import argparse

from rich.console import Console
from rich.panel import Panel


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--language", help="Specify the language (en/nl)")
    parser.add_argument(
        "--mmdd", default=False, action="store_true", help="Use mm/dd instead of dd/mm"
    )
    args = parser.parse_args()

    if args.language:
        language = args.language
        if language not in ["en", "nl"]:
            raise Exception("Language must be 'en' or 'nl'")
    else:
        args.language = "en"
    return args


def format_date(date, mmdd=False):
    if mmdd:
        return date.strftime("%m/%d")
    else:
        return date.strftime("%d/%m")


def print_box(title, content):
    console = Console()
    panel = Panel(
        content,
        title=title,
        style="bold green",
        title_align="left",
        width=50,
    )
    console.print(panel)
