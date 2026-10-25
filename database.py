import sqlite3
from pathlib import Path


DATABASE_PATH = Path(__file__).resolve().parent / "league.db"


def get_connection() -> sqlite3.Connection:
    database_uri = f"{DATABASE_PATH.as_uri()}?mode=rw"
    connection = sqlite3.connect(database_uri, uri=True)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection
