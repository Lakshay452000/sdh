from app.retrieval.retriever import retrieve_vector_context
from app.services.gemini_service import GeminiService
from app.schemas.rag_response import (
    RagResponse
)

class RagService:

    def __init__(self):
        self.gemini_service = GeminiService()

    def ask(self, question: str) -> RagResponse:

        chunks = retrieve_vector_context(question)
        context = "\n\n".join(
            chunk.content
            for chunk in chunks
        )

        prompt = f"""
You are a System Design assistant.

Answer using ONLY the provided context.

Context:
{context}

Question:
{question}
"""

        answer = self.gemini_service.ask(prompt)

        sources = []

        for chunk in chunks:

            source = (
                f"{chunk.source} "
                f"(chunk {chunk.chunk_number})"
            )

            if source not in sources:
                sources.append(source)

        return RagResponse(
            answer=answer,
            sources=sources,
            retrieved_chunks=chunks
        )