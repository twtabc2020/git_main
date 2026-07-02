import json
from pathlib import Path
import requests

config = json.loads(Path(__file__).with_name("staging_config.json").read_text(encoding="utf-8"))

def authenticate_user(username, password):
    payload = {
        "username": username,
        "password": password
    }

    response = requests.post(config["API_URL"] + "auth", json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Authentication failed", "status_code": response.status_code}


if __name__ == "__main__":
    result = authenticate_user(config["AUTH_USERNAME"], config["AUTH_PASSWORD"])
    print(result)
