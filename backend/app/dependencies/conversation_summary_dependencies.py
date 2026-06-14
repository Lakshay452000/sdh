from app.services.gemini_service import (
    GeminiService
)

from app.memory.services.conversation_summary_service import (
    ConversationSummaryService
)

gemini_service = GeminiService()

conversation_summary_service = (
    ConversationSummaryService(
        gemini_service
    )
)