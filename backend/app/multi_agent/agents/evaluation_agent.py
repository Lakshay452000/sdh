from app.architecture.architecture_service import (
    ArchitectureService
)


class EvaluationAgent:

    def __init__(
        self,
        architecture_service: ArchitectureService
    ):
        self._architecture_service = (
            architecture_service
        )

    async def execute(
        self,
        architecture_description: str,
        review_findings: str
    ):

        return await (
            self._architecture_service
            .evaluate(
                architecture_description=
                    architecture_description,
                review_findings=
                    review_findings
            )
        )