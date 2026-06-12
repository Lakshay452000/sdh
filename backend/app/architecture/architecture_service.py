from app.architecture.models import (
    ArchitectureEvaluation, ArchitectureReviewResponse
)
from app.architecture.prompts import (
    ARCHITECTURE_EVALUATION_PROMPT,
    ARCHITECTURE_ANALYSIS_PROMPT
)

from app.utils.json_utils import (
    extract_json
)
from app.utils.json_utils import (
    extract_json
)

class ArchitectureService:

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
    
    async def evaluate(
            self,
            architecture_description: str,
            review_findings: str
    ) -> ArchitectureEvaluation:

        prompt = (
            ARCHITECTURE_EVALUATION_PROMPT.format(
                architecture_description=architecture_description,
                review_findings=review_findings
            )
        )

        response = (
            self.gemini_service.ask(
                prompt
            )
        )

        return ArchitectureEvaluation(
            **extract_json(response)
        )

    