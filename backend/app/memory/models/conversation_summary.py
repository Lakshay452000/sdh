from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class ConversationSummary(Base):
    __tablename__ = "conversation_summaries"

    session_id: Mapped[str] = mapped_column(
        primary_key=True
    )

    summary: Mapped[str] = mapped_column(
        Text
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )