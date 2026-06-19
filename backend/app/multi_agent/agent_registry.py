from app.multi_agent.agents.review_agent import (
    ReviewAgent
)
from app.multi_agent.agents.evaluation_agent import (
    EvaluationAgent
)
from app.multi_agent.agents.correction_agent import (
    CorrectionAgent
)
from app.multi_agent.agents.verifier_agent import (
    VerifierAgent
)

from app.dependencies.architecture_dependencies import (
    architecture_service
)
from app.dependencies.rag_dependencies import (
    gemini_service
)

from app.multi_agent.agents.mermaid_agent import (
    MermaidAgent
)

review_agent = ReviewAgent(
    architecture_service
)

evaluation_agent = EvaluationAgent(
    architecture_service
)

correction_agent = CorrectionAgent(
    architecture_service
)

verifier_agent = VerifierAgent(
    gemini_service
)

mermaid_agent = MermaidAgent(
    architecture_service
)