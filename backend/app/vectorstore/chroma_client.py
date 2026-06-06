import chromadb
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CHROMA_DB_PATH = BASE_DIR / "chroma_db"

_client = chromadb.PersistentClient(
    path=CHROMA_DB_PATH
)


def get_chroma_client():
    return _client