from pydantic import BaseModel


class InterviewEvaluationResponse(
    BaseModel
):
    strengths: list[str]
    weaknesses: list[str]
    missing_concepts: list[str]
    score: int