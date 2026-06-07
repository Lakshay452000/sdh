from app.retrieval.retriever import (
    retrieve_vector_context
)

from app.retrieval.bm25_retriever import (
    BM25Retriever
)

from app.retrieval.rrf import (
    reciprocal_rank_fusion
)

from app.schemas.retrieved_chunk import (
    RetrievedChunk
)

from app.services.query_expansion_service import (
    QueryExpansionService
)

from app.schemas.metadata_filter import (
    MetadataFilter
)

class HybridRetriever:

    def __init__(self):

        self.bm25_retriever = (
            BM25Retriever()
        )

        self.query_expansion_service = (
            QueryExpansionService()
        )

    def retrieve(
        self,
        query: str,
        top_k: int = 10,
        metadata_filter: MetadataFilter | None = None
    ) -> list[RetrievedChunk]:

        # expanded_queries = (
        #     self.query_expansion_service
        #     .generate_queries(
        #         query
        #     )
        # )
        expanded_queries = [query]

        all_vector_chunks = []

        all_bm25_chunks = []

        for expanded_query in expanded_queries:

            vector_chunks = (
                retrieve_vector_context(
                    query=expanded_query,
                    top_k=top_k,
                    metadata_filter=metadata_filter
                )
            )

            bm25_chunks = (
                self.bm25_retriever.retrieve(
                    query=expanded_query,
                    top_k=top_k,
                    metadata_filter=metadata_filter
                )
            )

            all_vector_chunks.extend(
                vector_chunks
            )

            all_bm25_chunks.extend(
                bm25_chunks
            )

        fused_chunks = (
            reciprocal_rank_fusion(
                vector_chunks=all_vector_chunks,
                bm25_chunks=all_bm25_chunks
            )
        )

        return fused_chunks[:top_k]