import json
from pathlib import Path

def get_project_root() -> Path:
    """自動往上尋找包含 .git 的專案根目錄"""
    for parent in Path(__file__).resolve().parents:
        if (parent / ".git").exists():
            return parent
        

    # 找不到 .git, 就回傳四層上層目錄
    return Path(__file__).resolve().parent.parent.parent.parent
