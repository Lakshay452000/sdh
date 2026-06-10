from pydantic import BaseModel, Field


class StartInterviewRequest(BaseModel):
    problem_name: str = Field(
        ...,
        min_length=1
    )