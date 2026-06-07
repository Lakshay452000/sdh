from app.retrieval.retriever import (
    retrieve_vector_context
)
from app.services.gemini_service import (
    GeminiService
)
from app.schemas.rag_response import (
    RagResponse
)
from app.retrieval.auto_merging_retriever import (
    AutoMergingRetriever
)
from app.retrieval.hybrid_retriever import (
    HybridRetriever
)
from app.retrieval.reranker import (
    Reranker
)
from app.schemas.metadata_filter import (
    MetadataFilter
)

class RagService:

    def __init__(self):

        self.gemini_service = (
            GeminiService()
        )
        self.auto_merging_retriever = (
            AutoMergingRetriever()
        )
        self.hybrid_retriever = (
            HybridRetriever()
        )

        self.reranker = (
            Reranker()
        )

    def ask(
        self,
        question: str,
        metadata_filter: MetadataFilter | None = None
    ) -> RagResponse:

        chunks = (
            self.hybrid_retriever
            .retrieve(
                query=question,
                top_k=10,
                metadata_filter=metadata_filter
            )
        )
        # print("\nAFTER HYBRID")
        # print(f"count={len(chunks)}")

        # for chunk in chunks:
        #     print(
        #         chunk.level,
        #         chunk.node_id[:8],
        #         chunk.content[:100]
        #     )

        if not chunks:

            return RagResponse(
                answer="No relevant information found.",
                sources=[],
                retrieved_chunks=[]
            )
        
        chunks = self.reranker.rerank(
            query=question,
            chunks=chunks,
            top_n=3
        )

        # print("\nAFTER RERANK")
        # print(f"count={len(chunks)}")

        # for chunk in chunks:

        #     print("=" * 100)
        #     print(chunk.node_id)
        #     print(chunk.content)
        
        final_chunks = (
            self.auto_merging_retriever
            .auto_merge(chunks)
        )

        # print("\nAFTER AUTO MERGE")
        # print(f"count={len(final_chunks)}")

        # for chunk in final_chunks:

        #     print(
        #         chunk.level,
        #         chunk.node_id[:8]
        #     )

        #     print(
        #         chunk.content[:1000]
        #     )

        context = "\n\n".join(
            chunk.content
            for chunk in final_chunks
        )

        # return RagResponse(
        #     answer="DEBUG MODE",
        #     sources=[
        #         f"{chunk.source} (level {chunk.level})"
        #         for chunk in final_chunks
        #     ],
        #     retrieved_chunks=final_chunks
        # )
    
        prompt = f"""
You are a System Design assistant.

Use ONLY the provided context.

If the answer is not explicitly present in the context,
respond exactly:

"I could not find the answer in the provided context."

Do not use prior knowledge.
Do not make assumptions.
Do not infer information that is not explicitly stated.

Context:
{context}

Question:
{question}
"""

        answer = self.gemini_service.ask(
            prompt
        )

        sources = []

        for chunk in final_chunks:

            source = (
                f"{chunk.source} "
                f"(level {chunk.level})"
            )

            if source not in sources:

                sources.append(
                    source
                )

        return RagResponse(
            answer=answer,
            sources=sources,
            retrieved_chunks=final_chunks
        )