from abc import (
    ABC,
    abstractmethod
)

from app.schemas.chat_message import (
    ChatMessage
)


class ConversationMemoryStore(ABC):

    @abstractmethod
    def get_messages(
        self,
        session_id: str
    ) -> list[ChatMessage]:
        pass

    @abstractmethod
    def add_messages(
        self,
        session_id: str,
        messages: list[ChatMessage]
    ) -> None:
        pass

    @abstractmethod
    def clear(
        self,
        session_id: str
    ) -> None:
        pass