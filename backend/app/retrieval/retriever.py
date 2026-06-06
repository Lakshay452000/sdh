from app.schemas.retrieved_chunk import (
    RetrievedChunk
)

from app.vectorstore.system_design_collection import (
    get_collection
)

from app.retrieval.reranker import Reranker

reranker = Reranker()

def retrieve_vector_context(
    query: str,
    top_k: int = 10,
    document_id: str | None = None
) -> list[RetrievedChunk]:

    collection = get_collection()

    query_params = {
        "query_texts": [query],
        "n_results": top_k
    }

    if document_id is not None:

        query_params["where"] = {
            "document_id": document_id
        }

    results = collection.query(
        **query_params
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    retrieved_chunks = []

    for document, metadata, distance in zip(
        documents,
        metadatas,
        distances
    ):

        retrieved_chunks.append(
            RetrievedChunk(
                content=document,
                source=metadata["source"],
                chunk_number=metadata["chunk_number"],
                distance=distance
            )
        )
    retrieved_chunks.sort(
        key=lambda chunk: chunk.distance
    )

    reranked_chunks = reranker.rerank(
        query=query,
        chunks=retrieved_chunks,
        top_n=5
    )

    return reranked_chunks  