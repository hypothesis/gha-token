import pytest

from gha_token.core import get_token  # pylint:disable=unused-import


class TestGetToken:
    def test_it(self):
        pass


@pytest.fixture(autouse=True)
def requests(mocker):
    return mocker.patch("gha_token.core.requests", autospec=True)
