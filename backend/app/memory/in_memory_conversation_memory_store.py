# app/memory/in_memory_conversation_memory_store.py

from collections import (
    defaultdict
)

from app.memory.conversation_memory_store import (
    ConversationMemoryStore
)

from app.schemas.chat_message import (
    ChatMessage
)


class InMemoryConversationMemoryStore(
    ConversationMemoryStore
):

    def __init__(self):
        self._messages: dict[
            str,
            list[ChatMessage]
        ] = defaultdict(list)

    def get_messages(
        self,
        session_id: str
    ) -> list[ChatMessage]:
        return self._messages.get(
            session_id,
            []
        )

    def add_messages(
        self,
        session_id: str,
        messages: list[ChatMessage]
    ) -> None:
        self._messages[
            session_id
        ].extend(messages)

    def clear(
        self,
        session_id: str
    ) -> None:
        self._messages.pop(
            session_id,
            None
        )