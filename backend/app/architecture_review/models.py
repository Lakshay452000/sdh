from pydantic import BaseModel


class ArchitectureReviewResponse(BaseModel):
    score: int
    summary: str
    components: list[str]
    data_flow: str
    architecture_type: str
    strengths: list[str]
    issues: list[str]
    missing_components: list[str]