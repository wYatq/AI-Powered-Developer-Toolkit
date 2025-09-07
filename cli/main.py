import subprocess
import click
from rich.console import Console
from ai_dev_toolkit.reviewer import code_review

console = Console(color_system="auto")


@click.command()
@click.option("--diff", is_flag=True, help="Review unstaged changes.")
def review(diff):
    """AI code-review for local changes."""
    if not diff:
        console.print("[yellow]Use --diff to review unstaged changes.[/]")
        raise click.Abort

    raw = subprocess.check_output(["git", "diff"], text=True)
    if not raw:
        console.print("[green]No changes to review.[/]")
        return

    console.print("[bold]▶ AI Code Review[/]")
    console.rule(style="dim white")
    result = code_review(raw)
    console.print(result)


@click.command()
def doc():
    """Stub for auto-doc generation."""
    console.print("[bold]▶ ai-doc[/] coming soon!")


if __name__ == "__main__":
    review()
