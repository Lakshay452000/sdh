from app.schemas.retrieved_chunk import (
    RetrievedChunk
)
from app.vectorstore.system_design_collection import (
    get_collection
)
from app.config.constants import AUTO_MERGING_LEVEL_SIZES
from app.schemas.metadata_filter import (
    MetadataFilter
)

leaf_level = (
    len(AUTO_MERGING_LEVEL_SIZES) - 1
)

def retrieve_vector_context(
    query: str,
    top_k: int = 10,
    metadata_filter: MetadataFilter | None = None
) -> list[RetrievedChunk]:

    collection = get_collection()

    conditions = []
    conditions.append(
        {
            "level": leaf_level
        }
    )
    if metadata_filter:

        if metadata_filter.document_id:

            conditions.append(
                {
                    "document_id":
                    metadata_filter.document_id
                }
            )

        if metadata_filter.file_name:

            conditions.append(
                {
                    "file_name":
                    metadata_filter.file_name
                }
            )

        if metadata_filter.chunk_type:

            conditions.append(
                {
                    "chunk_type":
                    metadata_filter.chunk_type
                }
            )

        # if metadata_filter.level is not None:

        #     conditions.append(
        #         {
        #             "level":
        #             metadata_filter.level
        #         }
        #     )

    if not conditions:

        where_clause = {
            "level": leaf_level
        }

    elif len(conditions) == 1:

        where_clause = conditions[0]

    else:

        where_clause = {
            "$and": conditions
        }

    query_params = {
        "query_texts": [query],
        "n_results": top_k,
        "where": where_clause
    }

    results = collection.query(
        **query_params
    )
    
    if not results["documents"][0]:

        return []
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
    retrieved_chunks.sort(
        key=lambda chunk: chunk.distance
    )

    return retrieved_chunks  