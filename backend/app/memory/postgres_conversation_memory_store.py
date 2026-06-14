from sqlalchemy import select

from app.database.database import SessionLocal

from app.memory.conversation_memory_store import (
    ConversationMemoryStore
)

from app.conversation.models.conversation import (
    Conversation
)

from app.conversation.models.message import (
    Message
)

from app.schemas.chat_message import (
    ChatMessage
)

from app.schemas.chat_role import (
    ChatRole
)


class PostgresConversationMemoryStore(
    ConversationMemoryStore
):

    def get_messages(
        self,
        session_id: str
    ) -> list[ChatMessage]:

        with SessionLocal() as db:

            messages = (
                db.execute(
                    select(Message)
                    .where(
                        Message.session_id
                        == session_id
                    )
                    .order_by(
                        Message.created_at.asc()
                    )
                )
                .scalars()
                .all()
            )

            return [
                ChatMessage(
                    role=ChatRole(
                        message.role
                    ),
                    content=message.content
                )
                for message in messages
            ]

    def add_messages(
        self,
        session_id: str,
        messages: list[ChatMessage]
    ) -> None:

        with SessionLocal() as db:

            conversation = (
                db.get(
                    Conversation,
                    session_id
                )
            )

            if conversation is None:

                conversation = (
                    Conversation(
                        session_id=session_id
                    )
                )

                db.add(
                    conversation
                )

            for message in messages:

                db.add(
                    Message(
                        session_id=session_id,
                        role=message.role.value,
                        content=message.content
                    )
                )

            db.commit()

    def clear(
        self,
        session_id: str
    ) -> None:

        with SessionLocal() as db:

            messages = (
                db.execute(
                    select(Message)
                    .where(
                        Message.session_id
                        == session_id
                    )
                )
                .scalars()
                .all()
            )

            for message in messages:
                db.delete(message)

            conversation = (
                db.get(
                    Conversation,
                    session_id
                )
            )

            if conversation:
                db.delete(
                    conversation
                )

            db.commit()