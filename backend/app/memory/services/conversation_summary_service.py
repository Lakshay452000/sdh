from sqlalchemy import select

from app.database.database import SessionLocal

from app.memory.models.conversation_summary import (
    ConversationSummary
)
from app.services.gemini_service import (
    GeminiService
)


class ConversationSummaryService:

    def __init__(
            self,
            gemini_service: GeminiService
        ):
            self._gemini_service = (
                gemini_service
            )

    def generate_summary(
        self,
        existing_summary: str,
        history_text: str
    ) -> str:

        prompt = f"""
    You are maintaining a conversation memory.

    Existing Summary:
    {existing_summary}

    New Conversation:
    {history_text}

    Update the summary.

    Keep:
    - Important user goals
    - Decisions made
    - Important context

    Return only the updated summary.
    """

        return (
            self._gemini_service.ask(
                prompt
            )
        )

    def save_summary(
        self,
        session_id: str,
        summary_text: str
    ) -> None:

        with SessionLocal() as db:

            summary = (
                db.get(
                    ConversationSummary,
                    session_id
                )
            )

            if summary is None:

                summary = (
                    ConversationSummary(
                        session_id=session_id,
                        summary=summary_text
                    )
                )

                db.add(summary)

            else:

                summary.summary = (
                    summary_text
                )

            db.commit()

    def get_summary(
        self,
        session_id: str
    ) -> str:

        with SessionLocal() as db:

            summary = (
                db.execute(
                    select(
                        ConversationSummary
                    ).where(
                        ConversationSummary.session_id
                        == session_id
                    )
                )
                .scalar_one_or_none()
            )

            if summary is None:
                return ""

            return summary.summary