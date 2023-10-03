from argparse import ArgumentParser
from importlib.metadata import version

from gha_token.core import get_token


def cli(_argv=None):
    parser = ArgumentParser(
        description="Get a temporary app installation access token for the GitHub API."
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=version("gha_token"),
    )
    parser.add_argument(
        "--app-id",
        required=True,
        help="your GitHub app's App ID, e.g. '123456'",
    )
    parser.add_argument(
        "--private-key",
        required=True,
        help="a private key belonging to your GitHub App, e.g. '-----BEGIN RSA PRIVATE KEY-----\nMIIEow...psy/kP\n-----END RSA PRIVATE KEY-----'",
    )
    parser.add_argument(
        "--installation-id",
        required=True,
        help="the ID of an installation of your GitHub app, e.g. '12345678'",
    )

    args = parser.parse_args(_argv)

    token = get_token(args.app_id, args.private_key, args.installation_id)

    print(token)

    return 0
