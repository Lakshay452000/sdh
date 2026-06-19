from app.services.gemini_service import (
    GeminiService
)


class VerifierAgent:

    def __init__(
        self,
        gemini_service: GeminiService
    ):
        self._gemini_service = (
            gemini_service
        )

    async def execute(
        self,
        review,
        correction
    ):

        prompt = f"""
Review Findings:
{review}

Correction:
{correction}

Determine whether the
correction addresses the
review findings.

Return a short assessment.
"""

        return (
            self._gemini_service.ask(
                prompt
            )
        )