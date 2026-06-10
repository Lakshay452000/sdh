from pydantic import BaseModel


class InterviewReport(BaseModel):
    overall_score: int

    strengths: list[str]

    improvement_areas: list[str]

    summary: str