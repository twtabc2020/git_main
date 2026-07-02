import requests
from python_project.api.module.config import load_config
from urllib.parse import urljoin

config = load_config()


def authenticate_user(username, password):
    payload = {
        "username": username,
        "password": password
    }

    auth_url = urljoin(config["API_URL"], "auth")
    response = requests.post(auth_url, json=payload)

    # 遇到非 200 的狀態碼時，直接拋出例外會是更好的錯誤處理方式
    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    result = authenticate_user(
        config["AUTH_USERNAME"],
        config["AUTH_PASSWORD"]
    )
    print(result)
