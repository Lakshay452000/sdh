from app.services.gemini_service import (
    GeminiService
)
from app.retrieval.hybrid_retriever import (
    HybridRetriever
)
from app.retrieval.reranker import (
    Reranker
)
from app.retrieval.auto_merging_retriever import (
    AutoMergingRetriever
)
from app.dependencies.conversation_memory import (
    conversation_memory_service
)
from app.services.rag_service import (
    RagService
)

gemini_service = GeminiService()

hybrid_retriever = HybridRetriever()

reranker = Reranker()

auto_merging_retriever = (
    AutoMergingRetriever()
)

rag_service = RagService(
    gemini_service=gemini_service,
    hybrid_retriever=hybrid_retriever,
    reranker=reranker,
    auto_merging_retriever=(
        auto_merging_retriever
    ),
    conversation_memory_service=(
        conversation_memory_service
    )
)