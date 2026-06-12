from pydantic import BaseModel


class ArchitectureEvaluationRequest(
    BaseModel
):
    architecture_description: str
    review_findings: str