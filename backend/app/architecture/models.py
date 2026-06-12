from pydantic import BaseModel, Field


class ArchitectureReviewResponse(BaseModel):
    score: int
    summary: str
    components: list[str]
    data_flow: str
    architecture_type: str
    strengths: list[str]
    issues: list[str]
    missing_components: list[str]
    recommendations: list[str]

class CategoryScore(BaseModel):
    category: str
    score: int = Field(
        ge=0,
        le=100
    )
    reasoning: str


class ArchitectureEvaluation(BaseModel):
    overall_score: int = Field(
        ge=0,
        le=100
    )

    category_scores: list[CategoryScore]

    strengths: list[str]

    weaknesses: list[str]

    recommendations: list[str]