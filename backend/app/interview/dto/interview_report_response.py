from pydantic import BaseModel


class InterviewReportResponse(
    BaseModel
):
    overall_score: int

    strengths: list[str]

    improvement_areas: list[str]

    summary: str