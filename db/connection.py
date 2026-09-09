from pathlib import Path
import os
import sqlite3

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent

load_dotenv(ROOT_DIR / ".env")


def create_connection():
    """Создает подключение к базе данных."""

    db_path = os.getenv("DB_PATH")

    if not db_path:
        raise ValueError(
            "Переменная окружения DB_PATH не задана. Проверьте файл .env."
        )

    database = ROOT_DIR / db_path

    return sqlite3.connect(database)