from app.services.gemini_service import (
    GeminiService
)

from app.memory.services.long_term_memory_service import (
    LongTermMemoryService
)

gemini_service = GeminiService()

long_term_memory_service = (
    LongTermMemoryService(
        gemini_service
    )
)