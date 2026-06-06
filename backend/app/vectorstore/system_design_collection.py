from app.vectorstore.chroma_client import (
    get_chroma_client
)

from app.embeddings.embedding_provider import (
    get_embedding_function
)
from app.config.constants import (
    SYSTEM_DESIGN_COLLECTION
)
COLLECTION_NAME = SYSTEM_DESIGN_COLLECTION


def get_collection():
    client = get_chroma_client()

    return client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=get_embedding_function()
    )


def delete_collection():
    client = get_chroma_client()

    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass