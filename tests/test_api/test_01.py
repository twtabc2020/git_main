import sys
from pathlib import Path

from python_project.api import get_home_status as get_home_status_module
from python_project.api import post_login_token as post_login_token_module

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))


def test_get_home_status_can_be_called():
    result = get_home_status_module.get_home_status()

    assert isinstance(result, int)


def test_post_login_token_can_be_called():
    result = post_login_token_module.authenticate_user(
        post_login_token_module.config["AUTH_USERNAME"],
        post_login_token_module.config["AUTH_PASSWORD"],
    )

    assert isinstance(result, dict)
