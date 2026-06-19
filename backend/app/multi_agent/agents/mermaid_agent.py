from app.architecture.architecture_service import (
    ArchitectureService
)


class MermaidAgent:

    def __init__(
        self,
        architecture_service: ArchitectureService
    ):
        self._architecture_service = (
            architecture_service
        )

    async def execute(
        self,
        architecture_description: str
    ):

        return await (
            self._architecture_service
            .generate_mermaid_diagram(
                architecture_description
            )
        )