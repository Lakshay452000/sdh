from fastapi import APIRouter, Depends

from app.interview.dto.start_interview_request import (
    StartInterviewRequest
)
from app.interview.dto.start_interview_response import (
    StartInterviewResponse
)
from app.dependencies.interview_dependencies import (
    get_interview_service
)
from app.interview.service.interview_service import (
    InterviewService
)
from app.interview.dto.interview_answer_request import (
    InterviewAnswerRequest
)
from app.interview.dto.interview_answer_response import (
    InterviewAnswerResponse
)
from app.interview.dto.interview_report_response import (
    InterviewReportResponse
)

router = APIRouter()
router = APIRouter(
    prefix="/interview",
    tags=["Interview"]
)


@router.post(
    "/start",
    response_model=StartInterviewResponse
)
def start_interview(
    request: StartInterviewRequest,
    interview_service: InterviewService = Depends(
        get_interview_service
    )
):
    return interview_service.start_interview(
        request.problem_name
    )

@router.post(
    "/answer",
    response_model=InterviewAnswerResponse
)
def answer_question(
    request: InterviewAnswerRequest,
    interview_service: InterviewService = Depends(
        get_interview_service
    )
):
    return (
        interview_service.answer_question(
            request.session_id,
            request.answer
        )
    )

@router.get(
    "/{session_id}/report",
    response_model=InterviewReportResponse
)
def generate_report(
    session_id: str,
    interview_service: InterviewService = Depends(
        get_interview_service
    )
):
    return (
        interview_service.generate_report(
            session_id
        )
    )