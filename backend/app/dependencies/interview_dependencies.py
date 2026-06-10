from app.dependencies.rag_dependencies import (
    gemini_service
)
from app.interview.repository.in_memory_interview_session_repository import (
    InMemoryInterviewSessionRepository
)
from app.interview.service.interview_question_generator import (
    InterviewQuestionGenerator
)
from app.interview.service.interview_service import (
    InterviewService
)
from app.interview.service.interview_stage_manager import (
    InterviewStageManager
)
from app.interview.service.interview_answer_evaluator import (
    InterviewAnswerEvaluator
)
from app.interview.service.interview_report_generator import (
    InterviewReportGenerator
)

stage_manager = (
    InterviewStageManager()
)

session_repository = (
    InMemoryInterviewSessionRepository()
)

question_generator = (
    InterviewQuestionGenerator(
        gemini_service
    )
)

answer_evaluator = (
    InterviewAnswerEvaluator(
        gemini_service
    )
)

report_generator = (
    InterviewReportGenerator()
)

interview_service = (
    InterviewService(
        session_repository,
        question_generator,
        stage_manager,
        answer_evaluator,
        report_generator
    )
)


def get_interview_service() -> InterviewService:
    return interview_service