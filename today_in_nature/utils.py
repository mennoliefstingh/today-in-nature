import argparse
import os
from rich.console import Console
from rich.panel import Panel


def install_in_shell():
    """
    Prompts the user for language and date format preferences, and adds a command to the user's shell config file
    to display a message of the day (motd) with information about today's date and a nature fact in the specified
    language and date format.

    Raises:
        Exception: If the user's shell is not supported, or if the user enters an invalid language or date format.
    """
    # Get shell type
    shell = os.environ["SHELL"]
    if "zsh" in shell:
        shell = "zsh"
    elif "bash" in shell:
        shell = "bash"
    else:
        raise Exception("Shell not supported")

    # Ask user for language
    language = input("Language (en/nl): ")
    if language not in ["en", "nl"]:
        raise Exception("Language must be 'en' or 'nl'")

    # Ask user for mmdd
    mmdd = input("Use mm/dd instead of dd/mm (y/n): ")
    if mmdd not in ["y", "n"]:
        raise Exception("Answer must be 'y' or 'n'")
    mmdd = mmdd == "y"

    # Add command to shell config
    command = f"today-in-nature --language {language}"
    if mmdd:
        command += " --mmdd"
    command += "\n"
    with open(os.path.expanduser(f"~/.{shell}rc"), "a") as f:
        f.write("# Today in nature motd (delete line below to disable)\n")
        f.write(command)
    print(f"Added command '{command.strip()}' to ~/.{shell}rc")
    print(f"Restart your shell (source ~/.{shell}rc) to see your new motd!")


def parse_args() -> argparse.Namespace:
    """
    Parse command line arguments. If --install is passed, install the command in the user's shell.

    Returns:
        argparse.Namespace: An object containing the parsed arguments:
        - language (str): The language to use (en/nl)
        - mmdd (bool): Whether to use mm/dd instead of dd/mm
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--language", help="Specify the language (en/nl)")
    parser.add_argument(
        "--mmdd", default=False, action="store_true", help="Use mm/dd instead of dd/mm"
    )
    parser.add_argument("--install", default=False, action="store_true", help="Install in shell")
    args = parser.parse_args()
    if args.install:
        install_in_shell()
        exit()

    if args.language:
        language = args.language
        if language not in ["en", "nl"]:
            raise Exception("Language must be 'en' or 'nl'")
    else:
        args.language = "en"
    return args


def format_date(date, mmdd=False):
    """
    Formats a date object as a string.

    Args:
        date (datetime.date): The date object to format.
        mmdd (bool, optional): If True, format the date as MM/DD. Otherwise, format as DD/MM.

    Returns:
        str: The formatted date string.
    """
    if mmdd:
        return date.strftime("%m/%d")
    else:
        return date.strftime("%d/%m")


def print_box(title, content):
    """
    Prints a box with a title and content.

    Args:
        title (str): The title of the box.
        content (str): The content to be displayed in the box.

    Returns:
        None
    """
    console = Console()
    panel = Panel(
        content,
        title=title,
        style="bold green",
        title_align="left",
        width=70,
    )
    console.print(panel)
