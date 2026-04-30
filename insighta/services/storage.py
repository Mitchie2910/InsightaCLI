from pathlib import Path
import json

CONFIG_DIR = Path.home() / ".insighta"
FILE = CONFIG_DIR / "credentials.json"


def save_credentials(data: dict):
    CONFIG_DIR.mkdir(exist_ok=True)
    FILE.write_text(json.dumps(data))


def load_credentials():
    if FILE.exists():
        return json.loads(FILE.read_text())
    return None


def clear_credentials():
    if FILE.exists():
        FILE.unlink()