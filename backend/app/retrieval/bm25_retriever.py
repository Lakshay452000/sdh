from rank_bm25 import BM25Okapi

from app.vectorstore.system_design_collection import (
    get_collection
)
from app.schemas.retrieved_chunk import (
    RetrievedChunk
)


class BM25Retriever:

    def __init__(self):

        self.collection = get_collection()

    def retrieve(
        self,
        query: str,
        top_k: int = 10
    ) -> list[RetrievedChunk]:

        results = self.collection.get(
            include=["documents", "metadatas"]
        )

        documents = results["documents"]
        metadatas = results["metadatas"]

        tokenized_documents = [
            document.lower().split()
            for document in documents
        ]

        bm25 = BM25Okapi(
            tokenized_documents
        )

        scores = bm25.get_scores(
            query.lower().split()
        )

        scored_documents = list(
            zip(
                documents,
                metadatas,
                scores
            )
        )

        scored_documents.sort(
            key=lambda item: item[2],
            reverse=True
        )

        chunks = []

        for document, metadata, score in scored_documents[:top_k]:

            chunks.append(
                RetrievedChunk(
                    content=document,
                    source=metadata["source"],
                    chunk_number=metadata["chunk_number"],
                    distance=0.0,
                    bm25_score=float(score)
                )
            )

        return chunks