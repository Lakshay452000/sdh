from datetime import datetime

from sqlalchemy import (
    String,
    DateTime,
    Integer,
    Text
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.base import Base


class LongTermMemory(Base):

    __tablename__ = (
        "long_term_memories"
    )

    id: Mapped[int] = (
        mapped_column(
            Integer,
            primary_key=True
        )
    )

    session_id: Mapped[str] = (
        mapped_column(
            String(100),
            index=True
        )
    )

    memory: Mapped[str] = (
        mapped_column(Text)
    )

    created_at: Mapped[datetime] = (
        mapped_column(
            DateTime,
            default=datetime.utcnow
        )
    )