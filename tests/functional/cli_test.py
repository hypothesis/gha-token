from subprocess import run


def test_help():
    """Test the gha-token --help command."""
    run(["gha-token", "--help"], check=True)


def test_version():
    """Test the gha-token --version command."""
    run(["gha-token", "--version"], check=True)
