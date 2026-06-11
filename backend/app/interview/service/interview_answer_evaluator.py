from app.utils.json_utils import (
    extract_json
)
from app.services.gemini_service import (
    GeminiService
)
from app.interview.model.interview_evaluation import (
    InterviewEvaluation
)
from app.interview.prompt.interview_prompts import (
    ANSWER_EVALUATION_PROMPT
)


class InterviewAnswerEvaluator:

    def __init__(
        self,
        gemini_service: GeminiService
    ):
        self.gemini_service = (
            gemini_service
        )

    def evaluate(
        self,
        problem_name: str,
        current_stage: str,
        question: str,
        answer: str
    ) -> InterviewEvaluation:

        prompt = (
            ANSWER_EVALUATION_PROMPT.format(
                problem_name=problem_name,
                current_stage=current_stage,
                question=question,
                answer=answer
            )
        )

        response = (
            self.gemini_service
                .ask(prompt)
        )
        print("Raw evaluation response******************:")
        print(response)

        return InterviewEvaluation(
            **self._extract_json(response)
        )

    def _extract_json(
        self,
        response: str
    ) -> dict:

        cleaned_response = (
            response
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        return InterviewEvaluation(
            **extract_json(response)
        )