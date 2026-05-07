"""Carrega variáveis de ambiente do arquivo config.env."""

from pathlib import Path

ROOT = Path(__file__).parent.parent
ENV_FILE = ROOT / "config.env"


def load_env(path: Path = ENV_FILE) -> dict:
    env = {}
    if not path.exists():
        return env
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            key, _, value = line.partition("=")
            env[key.strip()] = value.strip()
    return env


settings = load_env()

APP_ENV = settings.get("APP_ENV", "development")
APP_NAME = settings.get("APP_NAME", "TaskManager")
APP_VERSION = settings.get("APP_VERSION", "1.0.0")
LOG_LEVEL = settings.get("LOG_LEVEL", "INFO")
