from app.retrieval.retriever import (
    retrieve_vector_context
)

from app.retrieval.bm25_retriever import (
    BM25Retriever
)

from app.retrieval.reranker import (
    Reranker
)


class HybridRetriever:

    def __init__(self):

        self.bm25_retriever = BM25Retriever()

        self.reranker = Reranker()

    def retrieve(
        self,
        query: str,
        top_k: int = 5
    ):

        vector_chunks = retrieve_vector_context(
            query=query,
            top_k=10
        )

        bm25_chunks = self.bm25_retriever.retrieve(
            query=query,
            top_k=10
        )

        merged_chunks = {}

        for chunk in vector_chunks:

            key = (
                chunk.source,
                chunk.chunk_number
            )

            merged_chunks[key] = chunk

        for chunk in bm25_chunks:

            key = (
                chunk.source,
                chunk.chunk_number
            )

            if key in merged_chunks:
                merged_chunks[key].bm25_score = (
                    chunk.bm25_score
                )
            else:
                merged_chunks[key] = chunk

        final_chunks = self.reranker.rerank(
            query=query,
            chunks=list(
                merged_chunks.values()
            ),
            top_n=top_k
        )

        return final_chunks