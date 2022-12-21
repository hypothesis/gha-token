import pytest

from gha_token.cli import cli

try:
    from importlib.metadata import version
except ModuleNotFoundError:
    from importlib_metadata import version


def test_it(capsys, get_token):
    get_token.return_value = "my_token"

    cli(
        [
            "--app-id",
            "my_app_id",
            "--private-key",
            "my_private_key",
            "--installation-id",
            "my_installation_id",
        ]
    )

    get_token.assert_called_once_with(
        "my_app_id", "my_private_key", "my_installation_id"
    )
    assert capsys.readouterr().out.strip() == "my_token"


def test_help():
    with pytest.raises(SystemExit) as exc_info:
        cli(["--help"])

    assert not exc_info.value.code


def test_version(capsys):
    with pytest.raises(SystemExit) as exc_info:
        cli(["--version"])

    assert capsys.readouterr().out.strip() == version("gha_token")
    assert not exc_info.value.code


@pytest.fixture(autouse=True)
def get_token(mocker):
    return mocker.patch("gha_token.cli.get_token")
