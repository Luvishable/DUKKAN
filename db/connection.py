import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / 'data' / 'dukkan.db'

def get_connection():
    return sqlite3.connect(DB_PATH)

