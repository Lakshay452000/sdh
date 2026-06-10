from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field

from app.interview.model.interview_message import InterviewMessage
from app.interview.model.interview_stage import InterviewStage
from app.interview.model.interview_evaluation import (
    InterviewEvaluation
)

class InterviewSession(BaseModel):
    session_id: str = Field(
        default_factory=lambda: str(uuid4())
    )

    problem_name: str

    current_stage: InterviewStage = (
        InterviewStage.REQUIREMENTS
    )

    conversation_history: list[
        InterviewMessage
    ] = Field(default_factory=list)

    evaluations: list[
        InterviewEvaluation
    ] = Field(
        default_factory=list
    )
    
    created_at: datetime = Field(
        default_factory=datetime.utcnow
    )

    is_completed: bool = False
    stage_message_count: int = 0