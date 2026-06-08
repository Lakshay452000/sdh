from app.memory.in_memory_conversation_memory_store import (
    InMemoryConversationMemoryStore
)

from app.services.conversation_memory_service import (
    ConversationMemoryService
)

memory_store = (
    InMemoryConversationMemoryStore()
)

conversation_memory_service = (
    ConversationMemoryService(
        memory_store
    )
)