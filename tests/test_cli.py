from typer.testing import CliRunner

from toolcall_bench import __version__
from toolcall_bench.cli import app

runner = CliRunner()


def test_version_flag_prints_installed_version():
    result = runner.invoke(app, ["--version"])

    assert result.exit_code == 0
    assert __version__ in result.output


def test_no_args_shows_help():
    result = runner.invoke(app, [])

    assert "Usage" in result.output
