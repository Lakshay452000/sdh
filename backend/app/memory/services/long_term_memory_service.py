from sqlalchemy import select

from app.database.database import SessionLocal
from app.memory.models.long_term_memory import (
    LongTermMemory
)
from app.services.gemini_service import (
    GeminiService
)


class LongTermMemoryService:

    def __init__(
        self,
        gemini_service: GeminiService
    ):
        self._gemini_service = (
            gemini_service
        )

    def extract_memory(
        self,
        conversation_text: str
    ) -> list[str]:

        prompt = f"""
Extract durable long-term facts.

Keep only:
- User goals
- User preferences
- Project decisions
- Important project state

Ignore temporary discussion.

Conversation:
{conversation_text}

Return one fact per line.
"""

        response = (
            self._gemini_service.ask(
                prompt
            )
        )

        return [
            line.strip()
            for line in response.splitlines()
            if line.strip()
        ]

    def save_memories(
        self,
        session_id: str,
        memories: list[str]
    ) -> None:

        with SessionLocal() as db:
            existing_memories = {
                memory.memory
                for memory in (
                    db.execute(
                        select(
                            LongTermMemory
                        ).where(
                            LongTermMemory.session_id
                            == session_id
                        )
                    )
                    .scalars()
                    .all()
                )
            }
            for memory in memories:

                if memory in existing_memories:
                    continue

                db.add(
                    LongTermMemory(
                        session_id=session_id,
                        memory=memory
                    )
                )

            db.commit()

    def get_memories(
        self,
        session_id: str
    ) -> list[str]:

        with SessionLocal() as db:

            results = (
                db.execute(
                    select(
                        LongTermMemory
                    ).where(
                        LongTermMemory.session_id
                        == session_id
                    )
                )
                .scalars()
                .all()
            )

            return [
                memory.memory
                for memory in results
            ]