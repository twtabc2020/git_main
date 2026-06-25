import requests


def add(a: int, b: int) -> int:
    return a + b


def greet(name: str) -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    url = "https://restful-booker.herokuapp.com/auth"

    payload = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(url, json=payload)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())