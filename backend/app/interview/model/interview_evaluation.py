from pydantic import BaseModel


class InterviewEvaluation(
    BaseModel
):
    strengths: list[str]
    weaknesses: list[str]
    missing_concepts: list[str]
    score: int