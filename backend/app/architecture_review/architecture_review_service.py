from app.architecture_review.models import (
    ArchitectureReviewResponse
)
from app.architecture_review.prompts import (
    ARCHITECTURE_ANALYSIS_PROMPT
)
from app.utils.json_utils import (
    extract_json
)

class ArchitectureReviewService:

    def __init__(
            self,
            gemini_service,
            rule_engine
    ):
        self.gemini_service = (
            gemini_service
        )

        self.rule_engine = (
            rule_engine
        )

    async def review_diagram(
            self,
            image_bytes: bytes
    ) -> ArchitectureReviewResponse:

        response = (
            self.gemini_service
                .analyze_image(
                    image_bytes=image_bytes,
                    prompt=ARCHITECTURE_ANALYSIS_PROMPT
                )
        )

        review = ArchitectureReviewResponse(
            **extract_json(response)
        )

        return self.rule_engine.execute(
            review
        )

    