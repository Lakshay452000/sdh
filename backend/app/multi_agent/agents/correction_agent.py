from app.architecture.architecture_service import (
    ArchitectureService
)


class CorrectionAgent:

    def __init__(
        self,
        architecture_service: ArchitectureService
    ):
        self._architecture_service = (
            architecture_service
        )

    async def execute(
        self,
        architecture_description,
        review,
        evaluation
    ):

        return await (
            self._architecture_service
            .generate_corrections(
                architecture_description=
                    architecture_description,
                review=review,
                evaluation=evaluation
            )
        )