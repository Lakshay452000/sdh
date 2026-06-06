from app.retrieval.retriever import retrieve_vector_context
from app.services.gemini_service import GeminiService
from app.schemas.rag_response import (
    RagResponse
)
from app.retrieval.sentence_window_retriever import (
    SentenceWindowRetriever
)

class RagService:

    def __init__(self):
        self.gemini_service = GeminiService()
        self.window_retriever = (
            SentenceWindowRetriever()
        )

    def ask(self, question: str) -> RagResponse:

        chunks = retrieve_vector_context(
            question
        )

        expanded_chunks = []

        for chunk in chunks:

            window_chunks = (
                self.window_retriever
                .retrieve_window(chunk)
            )

            expanded_chunks.extend(
                window_chunks
            )

        unique_chunks = {}

        for chunk in expanded_chunks:

            key = (
                chunk.source,
                chunk.chunk_number
            )

            unique_chunks[key] = chunk

        final_chunks = sorted(
            unique_chunks.values(),
            key=lambda chunk: (
                chunk.source,
                chunk.chunk_number
            )
        )

        print(
            [
                chunk.chunk_number
                for chunk in final_chunks
            ]
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

        answer = self.gemini_service.ask(prompt)

        sources = []

        for chunk in final_chunks:

            source = (
                f"{chunk.source} "
                f"(chunk {chunk.chunk_number})"
            )

            if source not in sources:
                sources.append(source)

        return RagResponse(
            answer=answer,
            sources=sources,
            retrieved_chunks=final_chunks
        )