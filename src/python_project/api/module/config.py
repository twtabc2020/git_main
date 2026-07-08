import json

from .lib import get_project_root


def load_config(config_name: str = "staging_config.json") -> dict:
    """
    從專案根目錄載入指定的 JSON 設定檔。
    """
    root = get_project_root()
    config_path = root / config_name

    if not config_path.exists():
        raise FileNotFoundError(f"找不到設定檔！請確認路徑是否正確：{config_path}")

    return json.loads(config_path.read_text(encoding="utf-8"))
