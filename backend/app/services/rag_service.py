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
from app.query_rewriting.query_rewriter import (
    QueryRewriter
)
from app.compression.context_compression_service import (
    ContextCompressionService
)
from app.memory.services.conversation_summary_service import (
    ConversationSummaryService
)
from app.memory.services.long_term_memory_service import (
    LongTermMemoryService
)

class RagService:

    def __init__(
        self,
        gemini_service: GeminiService,
        hybrid_retriever: HybridRetriever,
        reranker: Reranker,
        auto_merging_retriever: AutoMergingRetriever,
        conversation_memory_service: ConversationMemoryService,
        query_rewriter: QueryRewriter,
        context_compression_service: ContextCompressionService,
        conversation_summary_service: ConversationSummaryService,
        long_term_memory_service: LongTermMemoryService
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

        self._query_rewriter = (
            query_rewriter
        )
        self._context_compression_service = (
            context_compression_service
        )
        self._conversation_summary_service = (
            conversation_summary_service
        )
        self._long_term_memory_service = (
            long_term_memory_service
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
        summary = (
            self._conversation_summary_service
            .get_summary(session_id)
        )
        long_term_memories = (
            self._long_term_memory_service
            .get_memories(session_id)
        )
        long_term_memory_text = "\n".join(
            long_term_memories
        )
        if history_text.strip():
            rewrite_context = f"""
            Long Term Memory:
            {long_term_memory_text}

            Conversation Summary:
            {summary}

            Recent Conversation:
            {history_text}
            """

            rewritten_question = (
                self._query_rewriter
                .rewrite(
                    question=question,
                    history=rewrite_context
                )
            )
        else:
            rewritten_question = question
        
        self._conversation_memory_service.add_messages(
            session_id=session_id,
            messages=[
                ChatMessage(
                    role=ChatRole.USER,
                    content=question
                )
            ]
        )
        
        retrieval_query = f"""
        Long Term Memory:
        {long_term_memory_text}

        Conversation Summary:
        {summary}

        Recent Conversation:
        {history_text}

        Current Question:
        {rewritten_question}
        """
        chunks = (
            self._hybrid_retriever
            .retrieve(
                query=retrieval_query,
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
            self._update_summary_if_needed(
                session_id=session_id,
                summary=summary
            )
            return RagResponse(
                answer=answer,
                sources=[],
                retrieved_chunks=[]
            )

        chunks = self._reranker.rerank(
            query=rewritten_question,
            chunks=chunks,
            top_n=5
        )
        final_chunks = (
            self._auto_merging_retriever
            .auto_merge(chunks)
        )
        final_chunks = (
            self._context_compression_service
            .compress(
                query=rewritten_question,
                chunks=final_chunks
            )
        )
        context = "\n\n".join(
            chunk.content
            for chunk in final_chunks
        )

        prompt = f"""
You are a System Design assistant.

Long Term Memory:
{long_term_memory_text}

Conversation Summary:
{summary}

Recent Conversation:
{history_text}

Retrieved Context:
{context}

Question:
{rewritten_question}

Use the following information sources in order:

1. Recent Conversation
2. Conversation Summary
3. Long Term Memory
4. Retrieved Context

Rules:

- For questions about previous messages, use Recent Conversation.
- For questions about long-running discussions, use Conversation Summary.
- For questions about user preferences, goals, or project state, use Long Term Memory.
- For knowledge questions, use Retrieved Context.
- Do not use prior knowledge.
- Do not make assumptions.
- Do not invent information.

If the answer cannot be found in any of the above information sources,
respond exactly:

"I could not find the answer."
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
        self._update_summary_if_needed(
            session_id=session_id,
            summary=summary
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
    
    def _update_summary_if_needed(
        self,
        session_id: str,
        summary: str
    ) -> None:

        message_count = len(
            self._conversation_memory_service
            .get_recent_messages(
                session_id=session_id,
                limit=10000
            )
        )

        if message_count % 4 == 0:

            latest_history = (
                self._conversation_memory_service
                .build_history_text(
                    session_id=session_id,
                    limit=100
                )
            )

            updated_summary = (
                self._conversation_summary_service
                .generate_summary(
                    existing_summary=summary,
                    history_text=latest_history
                )
            )

            self._conversation_summary_service.save_summary(
                session_id=session_id,
                summary_text=updated_summary
            )
            memories = (
                self._long_term_memory_service
                .extract_memory(
                    latest_history
                )
            )

            self._long_term_memory_service.save_memories(
                session_id=session_id,
                memories=memories
            )