import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

_client = chromadb.PersistentClient(path="./chroma_db")

_embedding_function = SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

_collection = _client.get_or_create_collection(
    name="documents",
    embedding_function=_embedding_function
)


def get_collection():
    return _collection