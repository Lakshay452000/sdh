from app.conversation.models.conversation import Conversation
from app.conversation.models.message import Message
from app.conversation.repositories.conversation_repository import (
    ConversationRepository
)


class ConversationService:

    def __init__(self):
        self.repository = ConversationRepository()

    def create_conversation(
        self,
        db,
        title: str
    ) -> Conversation:

        conversation = Conversation(
            title=title
        )

        return self.repository.create_conversation(
            db,
            conversation
        )

    def get_conversation(
        self,
        db,
        conversation_id: int
    ):
        conversation = self.repository.get_conversation(
            db,
            conversation_id
        )

        if not conversation:
            raise ValueError(
                f"Conversation {conversation_id} not found"
            )

        messages = self.repository.get_messages(
            db,
            conversation_id
        )

        return conversation, messages

    def save_message(
        self,
        db,
        conversation_id: int,
        role: str,
        content: str
    ):
        message = Message(
            conversation_id=conversation_id,
            role=role,
            content=content
        )

        return self.repository.save_message(
            db,
            message
        )