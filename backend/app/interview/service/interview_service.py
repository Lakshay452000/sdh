from datetime import datetime
from app.interview.dto.start_interview_response import (
    StartInterviewResponse
)
from app.interview.model.interview_message import (
    InterviewMessage
)
from app.interview.model.interview_session import (
    InterviewSession
)
from app.interview.dto.interview_answer_response import (
    InterviewAnswerResponse
)
from app.exceptions.interview_session_not_found_exception import (
    InterviewSessionNotFoundException
)
from app.interview.dto.interview_report_response import (
    InterviewReportResponse
)

class InterviewService:

    def __init__(
        self,
        repository,
        question_generator,
        stage_manager,
        answer_evaluator,
        report_generator
    ):
        self.repository = repository
        self.question_generator = (
            question_generator
        )
        self.stage_manager = (
            stage_manager
        )
        self.answer_evaluator = (
            answer_evaluator
        )
        self.report_generator = (
            report_generator
        )

    def start_interview(
        self,
        problem_name: str
    ) -> StartInterviewResponse:

        session = InterviewSession(
            problem_name=problem_name
        )

        first_question = (
            self.question_generator
                .generate_question(
                    session
                )
        )

        session.conversation_history.append(
            InterviewMessage(
                role="interviewer",
                content=first_question,
                timestamp=datetime.utcnow()
            )
        )

        self.repository.save(session)

        return StartInterviewResponse(
            session_id=session.session_id,
            first_question=first_question
        )
    
    def answer_question(
        self,
        session_id: str,
        answer: str
    ) -> InterviewAnswerResponse:

        session = self.repository.get(
            session_id
        )

        if session is None:
            raise (
                InterviewSessionNotFoundException(
                    f"Session {session_id} not found"
                )
            )

        session.conversation_history.append(
            InterviewMessage(
                role="user",
                content=answer,
                timestamp=datetime.utcnow()
            )
        )
        session.stage_message_count += 1
        last_question = (
            session.conversation_history[-2]
            .content
        )

        evaluation = (
            self.answer_evaluator.evaluate(
                problem_name=session.problem_name,
                current_stage=(
                    session.current_stage.value
                ),
                question=last_question,
                answer=answer
            )
        )

        session.evaluations.append(
            evaluation
        )
        
        self.stage_manager.advance_stage_if_needed(
            session
        )

        next_question = (
            self.question_generator
                .generate_question(
                    session
                )
        )

        session.conversation_history.append(
            InterviewMessage(
                role="interviewer",
                content=next_question,
                timestamp=datetime.utcnow()
            )
        )

        self.repository.save(
            session
        )

        return InterviewAnswerResponse(
            next_question=next_question,
            current_stage=session.current_stage.value,
            evaluation=evaluation
        )
    
    def generate_report(
        self,
        session_id: str
    ) -> InterviewReportResponse:

        session = self.repository.get(
            session_id
        )

        if session is None:
            raise (
                InterviewSessionNotFoundException(
                    f"Session {session_id} not found"
                )
            )

        report = (
            self.report_generator
                .generate(
                    session
                )
        )

        return InterviewReportResponse(
            overall_score=(
                report.overall_score
            ),
            strengths=(
                report.strengths
            ),
            improvement_areas=(
                report.improvement_areas
            ),
            summary=(
                report.summary
            )
        )