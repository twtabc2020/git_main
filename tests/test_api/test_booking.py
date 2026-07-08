import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from python_project.api import post_booking as post_booking_module  # noqa: E402


def test_post_booking_returns_booking_info():
    booking_data = {
        "roomid": 1,
        "firstname": "test",
        "lastname": "test",
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2026-07-13",
            "checkout": "2026-07-14",
        },
        "email": "test@ggmail.com",
        "phone": "11111111111",
    }

    result = post_booking_module.post_booking(token=None, booking_data=booking_data)

    assert isinstance(result, dict)


def test_post_booking_with_empty_data_returns_error():
    booking_data = {}

    result = post_booking_module.post_booking(token=None, booking_data=booking_data)

    assert "errors" in result
