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

class RagService:

    def __init__(self):

        self.gemini_service = (
            GeminiService()
        )
        self.auto_merging_retriever = (
            AutoMergingRetriever()
        )

    def ask(
        self,
        question: str
    ) -> RagResponse:

        chunks = (
            retrieve_vector_context(
                question
            )
        )

        final_chunks = (
            self.auto_merging_retriever
            .auto_merge(chunks)
        )
        context = "\n\n".join(
            chunk.content
            for chunk in final_chunks
        )

        prompt = f"""
You are a System Design assistant.

Answer using ONLY the provided context.

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