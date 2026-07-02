import json
import requests
from python_project.api.module.lib import get_project_root


ROOT = get_project_root()
CONFIG_PATH = ROOT / "staging_config.json"

if not CONFIG_PATH.exists():
    raise FileNotFoundError(f"找不到設定檔！請確認路徑是否正確：{CONFIG_PATH}")

config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def get_home_status():
    response = requests.get(config["HOME_URL"])
    return response.status_code


if __name__ == "__main__":
    status_code = get_home_status()

    if status_code == 200:
        print("Home page is accessible.")
    else:
        print(f"Error accessing home page. Status code: {status_code}")
