from app.dependencies.rag_dependencies import (
    rag_service
)


class RetrievalTool:

    def execute(
        self,
        query: str
    ) -> str:

        response = rag_service.ask(
            session_id="agent-session",
            question=query
        )

        return response.answer