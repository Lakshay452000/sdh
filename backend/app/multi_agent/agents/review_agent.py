from app.architecture.architecture_service import (
    ArchitectureService
)


class ReviewAgent:

    def __init__(
        self,
        architecture_service: ArchitectureService
    ):
        self._architecture_service = (
            architecture_service
        )

    async def execute(
        self,
        image_bytes: bytes
    ):

        return await (
            self._architecture_service
            .review_diagram(
                image_bytes
            )
        )