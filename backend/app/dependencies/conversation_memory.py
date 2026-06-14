from app.memory.postgres_conversation_memory_store import (
    PostgresConversationMemoryStore
)

from app.services.conversation_memory_service import (
    ConversationMemoryService
)

memory_store = (
    PostgresConversationMemoryStore()
)

conversation_memory_service = (
    ConversationMemoryService(
        memory_store
    )
)