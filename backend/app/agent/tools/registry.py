from app.agent.tools.retrieval_tool import (
    RetrievalTool
)

from app.agent.tools.memory_tool import (
    MemoryTool
)
from app.agent.tools.architecture_review_tool import (
    ArchitectureReviewTool
)
from app.agent.tools.evaluation_tool import (
    EvaluationTool
)

TOOL_REGISTRY = {
    "rag": RetrievalTool(),
    "memory": MemoryTool(),
    "architecture_review": ArchitectureReviewTool(),
    "evaluation": EvaluationTool()
}