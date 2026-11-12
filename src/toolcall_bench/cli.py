"""Command-line entry point. Commands are added one milestone at a time."""

from typing import Annotated

import typer

from toolcall_bench import __version__

app = typer.Typer(
    name="tcb",
    help="Deterministic tool-calling evals for local LLMs.",
    no_args_is_help=True,
)


def _print_version(value: bool) -> None:
    if value:
        typer.echo(f"toolcall-bench {__version__}")
        raise typer.Exit


@app.callback()
def main(
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            callback=_print_version,
            is_eager=True,
            help="Show the installed version and exit.",
        ),
    ] = False,
) -> None:
    """Deterministic tool-calling evals for local LLMs."""
