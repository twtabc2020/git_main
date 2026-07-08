import requests
from python_project.api.module.config import load_config
from urllib.parse import urljoin

config = load_config()


def post_booking(token, booking_data=None):
    payload = booking_data
    booking_url = urljoin(config["HOME_URL"], "api/booking")
    response = requests.post(booking_url, json=payload)

    # response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    result = post_booking(
        token=None,
        booking_data={
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
        },
    )
    print(result)
