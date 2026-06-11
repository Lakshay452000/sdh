from app.dependencies.rag_dependencies import gemini_service

from app.architecture_review.architecture_review_service import (
    ArchitectureReviewService
)

from app.architecture_review.rules.rule_engine import (
    RuleEngine
)

rule_engine = RuleEngine()

architecture_review_service = (
    ArchitectureReviewService(
        gemini_service=gemini_service,
        rule_engine=rule_engine
    )
)