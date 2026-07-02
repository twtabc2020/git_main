import json
from pathlib import Path
import requests

def get_project_root() -> Path:
    """自動往上尋找包含 .git 的專案根目錄"""
    for parent in Path(__file__).resolve().parents:
        if (parent / ".git").exists():
            return parent
    # 找不到 .git, 就回傳四層上層目錄
    return Path(__file__).resolve().parent.parent.parent.parent

ROOT = get_project_root()
CONFIG_PATH = ROOT / "staging_config.json"

if not CONFIG_PATH.exists():
    raise FileNotFoundError(f"找不到設定檔！請確認路徑是否正確：{CONFIG_PATH}")

config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


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
