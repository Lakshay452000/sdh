from app.dependencies.rag_dependencies import gemini_service

from app.architecture.architecture_service import (
    ArchitectureService
)

from app.architecture.rules.rule_engine import (
    RuleEngine
)

rule_engine = RuleEngine()

architecture_service = (
    ArchitectureService(
        gemini_service=gemini_service,
        rule_engine=rule_engine
    )
)