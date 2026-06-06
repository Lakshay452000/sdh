from app.retrieval.hybrid_retriever import (
    HybridRetriever
)
from app.services.query_expansion_service import (
    QueryExpansionService
)

class MultiQueryRetriever:

    def __init__(self):

        self.hybrid_retriever = (
            HybridRetriever()
        )
        self.query_expansion_service = (
            QueryExpansionService()
        )

    def retrieve(
        self,
        question: str,
        top_k: int = 5
    ):

        queries = (
            self.query_expansion_service
            .generate_queries(question)
        )

        print(queries)
        all_chunks = {}

        for query in queries:

            chunks = self.hybrid_retriever.retrieve(
                query=query,
                top_k=10
            )

            for chunk in chunks:

                key = (
                    chunk.source,
                    chunk.chunk_number
                )

                all_chunks[key] = chunk

        return list(
            all_chunks.values()
        )[:top_k]