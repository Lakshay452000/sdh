from app.interview.model.interview_session import (
    InterviewSession
)
from app.interview.repository.interview_session_repository import (
    InterviewSessionRepository
)


class InMemoryInterviewSessionRepository(
    InterviewSessionRepository
):

    def __init__(self):
        self.sessions: dict[
            str,
            InterviewSession
        ] = {}

    def save(
        self,
        session: InterviewSession
    ) -> None:
        self.sessions[
            session.session_id
        ] = session

    def get(
        self,
        session_id: str
    ) -> InterviewSession | None:
        return self.sessions.get(session_id)