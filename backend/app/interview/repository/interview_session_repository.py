from abc import ABC, abstractmethod

from app.interview.model.interview_session import (
    InterviewSession
)


class InterviewSessionRepository(ABC):

    @abstractmethod
    def save(
        self,
        session: InterviewSession
    ) -> None:
        pass

    @abstractmethod
    def get(
        self,
        session_id: str
    ) -> InterviewSession | None:
        pass