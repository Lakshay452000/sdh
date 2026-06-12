from pydantic import BaseModel
from app.architecture.models import ( 
    ArchitectureReviewResponse, 
    ArchitectureEvaluation
)

class ArchitectureEvaluationRequest(
    BaseModel
):
    architecture_description: str
    review_findings: str

class ArchitectureChange(BaseModel):
    issue: str
    applied_fix: str
    reasoning: str

class ArchitectureCorrection(BaseModel):
    corrected_architecture: str
    changes: list[ArchitectureChange]
    summary: ArchitectureSummary

class ArchitectureCorrectionRequest(BaseModel):
    architecture_description: str
    review: ArchitectureReviewResponse
    evaluation: ArchitectureEvaluation

class ArchitectureDiagram(BaseModel):
    mermaid_diagram: str

class MermaidDiagramRequest(BaseModel):
    architecture_description: str

class ArchitectureSummary(BaseModel):
    major_improvements: list[str]
    expected_benefits: list[str]
    tradeoffs: list[str]