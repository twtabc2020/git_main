import json
from pathlib import Path
import requests

config = json.loads(Path(__file__).with_name("staging_config.json").read_text(encoding="utf-8"))

def get_home_status():
    response = requests.get(config["HOME_URL"])
    return response.status_code

if __name__ == "__main__":
    status_code = get_home_status()

    if status_code == 200:
        print("Home page is accessible.")
    else:
        print(f"Error accessing home page. Status code: {status_code}")

