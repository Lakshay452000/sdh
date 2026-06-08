from app.query_rewriting.query_rewriter import (
    QueryRewriter
)

from app.services.gemini_service import (
    GeminiService
)


class GeminiQueryRewriter(
    QueryRewriter
):

    def __init__(
        self,
        gemini_service: GeminiService
    ):
        self._gemini_service = (
            gemini_service
        )

    def rewrite(
        self,
        question: str,
        history: str
    ) -> str:

        prompt = f"""
Conversation History:
{history}

Current Question:
{question}

Rewrite the current question into a
standalone question.

If the question is already standalone,
return it unchanged.

Return ONLY the rewritten question.
"""

        return (
            self._gemini_service
            .ask(prompt)
            .strip()
        )