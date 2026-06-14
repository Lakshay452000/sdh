from sqlalchemy.orm import Session

from app.conversation.models.conversation import Conversation
from app.conversation.models.message import Message


class ConversationRepository:

    def create_conversation(
        self,
        db: Session,
        conversation: Conversation
    ) -> Conversation:
        db.add(conversation)
        db.commit()
        db.refresh(conversation)

        return conversation

    def get_conversation(
        self,
        db: Session,
        conversation_id: int
    ) -> Conversation | None:
        return (
            db.query(Conversation)
            .filter(Conversation.id == conversation_id)
            .first()
        )

    def get_all_conversations(
        self,
        db: Session
    ) -> list[Conversation]:
        return (
            db.query(Conversation)
            .order_by(Conversation.created_at.desc())
            .all()
        )

    def delete_conversation(
        self,
        db: Session,
        conversation: Conversation
    ) -> None:
        db.delete(conversation)
        db.commit()

    def save_message(
        self,
        db: Session,
        message: Message
    ) -> Message:
        db.add(message)
        db.commit()
        db.refresh(message)

        return message

    def get_messages(
        self,
        db: Session,
        conversation_id: int
    ) -> list[Message]:
        return (
            db.query(Message)
            .filter(Message.conversation_id == conversation_id)
            .order_by(Message.created_at.asc())
            .all()
        )