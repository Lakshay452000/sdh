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
from app.services.conversation_memory_service import (
    ConversationMemoryService
)
from app.schemas.chat_message import (
    ChatMessage
)
from app.schemas.chat_role import (
    ChatRole
)


class RagService:

    def __init__(
        self,
        gemini_service: GeminiService,
        hybrid_retriever: HybridRetriever,
        reranker: Reranker,
        auto_merging_retriever: AutoMergingRetriever,
        conversation_memory_service:
            ConversationMemoryService
    ):
        self._gemini_service = (
            gemini_service
        )

        self._hybrid_retriever = (
            hybrid_retriever
        )

        self._reranker = (
            reranker
        )

        self._auto_merging_retriever = (
            auto_merging_retriever
        )

        self._conversation_memory_service = (
            conversation_memory_service
        )

    def ask(
        self,
        session_id: str,
        question: str,
        metadata_filter: MetadataFilter | None = None
    ) -> RagResponse:

        history_text = (
            self._conversation_memory_service
            .build_history_text(
                session_id=session_id
            )
        )
        self._conversation_memory_service.add_messages(
            session_id=session_id,
            messages=[
                ChatMessage(
                    role=ChatRole.USER,
                    content=question
                )
            ]
        )

        chunks = (
            self._hybrid_retriever
            .retrieve(
                query=question,
                top_k=10,
                metadata_filter=metadata_filter
            )
        )

        if not chunks:

            answer = (
                "No relevant information found."
            )

            self._conversation_memory_service.add_messages(
                session_id=session_id,
                messages=[
                    ChatMessage(
                        role=ChatRole.ASSISTANT,
                        content=answer
                    )
                ]
            )

            return RagResponse(
                answer=answer,
                sources=[],
                retrieved_chunks=[]
            )

        chunks = self._reranker.rerank(
            query=question,
            chunks=chunks,
            top_n=3
        )

        final_chunks = (
            self._auto_merging_retriever
            .auto_merge(chunks)
        )

        context = "\n\n".join(
            chunk.content
            for chunk in final_chunks
        )

        prompt = f"""
You are a System Design assistant.

Conversation History:
{history_text}

The conversation history is provided only to help
understand follow-up questions and references such as
"it", "that", "those", and similar pronouns.

Use ONLY the provided context to answer.

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

        answer = self._gemini_service.ask(
            prompt
        )

        self._conversation_memory_service.add_messages(
            session_id=session_id,
            messages=[
                ChatMessage(
                    role=ChatRole.ASSISTANT,
                    content=answer
                )
            ]
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