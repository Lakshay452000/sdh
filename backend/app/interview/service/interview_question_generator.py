from app.services.gemini_service import GeminiService
from app.interview.model.interview_session import (
    InterviewSession
)
from app.interview.model.interview_session import (
    InterviewSession
)
from app.interview.prompt.interview_prompts import (
    QUESTION_GENERATION_PROMPT
)

class InterviewQuestionGenerator:

    def __init__(
        self,
        gemini_service: GeminiService
    ):
        self.gemini_service = gemini_service


    def generate_question(
        self,
        session: InterviewSession
    ) -> str:

        prompt = QUESTION_GENERATION_PROMPT.format(
            problem_name=session.problem_name,
            current_stage=session.current_stage.value,
            conversation=(
                self._build_conversation(
                    session
                )
            )
        )

        return self.gemini_service.ask(
            prompt
        )
    
    def _build_conversation(
        self,
        session: InterviewSession
    ) -> str:

        return "\n".join(
            f"{message.role}: {message.content}"
            for message in (
                session.conversation_history[-10:]
            )
        )