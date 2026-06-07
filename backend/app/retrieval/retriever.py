from app.schemas.retrieved_chunk import (
    RetrievedChunk
)
from app.vectorstore.system_design_collection import (
    get_collection
)
from app.retrieval.reranker import Reranker
from app.config.constants import AUTO_MERGING_LEVEL_SIZES

reranker = Reranker()
leaf_level = (
    len(AUTO_MERGING_LEVEL_SIZES) - 1
)

def retrieve_vector_context(
    query: str,
    top_k: int = 10,
    document_id: str | None = None
) -> list[RetrievedChunk]:

    collection = get_collection()

    query_params = {
        "query_texts": [query],
        "n_results": top_k,
        "where": {
            "level": leaf_level
        }
    }

    if document_id is not None:
        query_params["where"] = {
            "$and": [
                {
                    "document_id": document_id
                },
                {
                    "level": leaf_level
                }
            ]
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
                node_id=metadata["node_id"],
                parent_id=metadata["parent_id"],
                level=metadata["level"],
                distance=distance
            )
        )
    for chunk in retrieved_chunks:
        print(
            chunk.level,
            chunk.node_id
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