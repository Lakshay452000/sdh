from app.memory.conversation_memory_store import (
    ConversationMemoryStore
)

from app.schemas.chat_message import (
    ChatMessage
)


class ConversationMemoryService:

    def __init__(
        self,
        memory_store: ConversationMemoryStore
    ):
        self._memory_store = memory_store

    def get_recent_messages(
        self,
        session_id: str,
        limit: int = 10
    ) -> list[ChatMessage]:

        messages = (
            self._memory_store
            .get_messages(session_id)
        )

        return messages[-limit:]

    def add_messages(
        self,
        session_id: str,
        messages: list[ChatMessage]
    ) -> None:
        self._memory_store.add_messages(
            session_id,
            messages
        )

    def build_history_text(
        self,
        session_id: str,
    limit: int = 10
    ) -> str:

        messages = self.get_recent_messages(
            session_id=session_id,
            limit=limit
        )

        return "\n".join(
            f"{message.role.value}: {message.content}"
            for message in messages
        )