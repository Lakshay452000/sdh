from pydantic import BaseModel, Field


class InterviewAnswerRequest(BaseModel):
    session_id: str = Field(...)

    answer: str = Field(
        ...,
        min_length=1
    )