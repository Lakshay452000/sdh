from chromadb.utils.embedding_functions import (
    SentenceTransformerEmbeddingFunction
)

_embedding_function = (
    SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
)


def get_embedding_function():
    return _embedding_function