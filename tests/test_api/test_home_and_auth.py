import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from python_project.api import get_home_status as get_home_status_module  # noqa: E402
from python_project.api import post_login_token as post_login_token_module  # noqa: E402


def test_get_home_status_can_be_called():
    result = get_home_status_module.get_home_status()

    assert isinstance(result, int)


def test_post_login_token_can_be_called():
    result = post_login_token_module.authenticate_user(
        post_login_token_module.config["AUTH_USERNAME"],
        post_login_token_module.config["AUTH_PASSWORD"],
    )

    assert isinstance(result, dict)
