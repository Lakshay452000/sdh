from app.architecture.schemas import (
    ArchitectureReviewResult, ArchitectureEvaluationResult
)

def build_architecture_correction_prompt(
    architecture: str,
    review: ArchitectureReviewResult,
    evaluation: ArchitectureEvaluationResult
) -> str:
    ...