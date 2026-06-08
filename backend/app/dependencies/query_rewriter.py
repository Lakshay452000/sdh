from app.dependencies.rag_dependencies import (
    gemini_service
)

from app.query_rewriting.gemini_query_rewriter import (
    GeminiQueryRewriter
)

query_rewriter = (
    GeminiQueryRewriter(
        gemini_service
    )
)