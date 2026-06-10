from app.interview.model.interview_report import (
    InterviewReport
)
from app.interview.model.interview_session import (
    InterviewSession
)


class InterviewReportGenerator:

    def generate(
        self,
        session: InterviewSession
    ) -> InterviewReport:

        if not session.evaluations:
            return InterviewReport(
                overall_score=0,
                strengths=[],
                improvement_areas=[],
                summary="No evaluations found."
            )

        scores = [
            evaluation.score
            for evaluation
            in session.evaluations
        ]

        strengths = []

        improvement_areas = []

        for evaluation in (
            session.evaluations
        ):
            strengths.extend(
                evaluation.strengths
            )

            improvement_areas.extend(
                evaluation.missing_concepts
            )

        overall_score = int(
            sum(scores)
            / len(scores)
        )

        return InterviewReport(
            overall_score=overall_score,
            strengths=list(
                set(strengths)
            )[:10],
            improvement_areas=list(
                set(improvement_areas)
            )[:10],
            summary=(
                f"Completed "
                f"{len(session.evaluations)} "
                f"evaluated interview rounds."
            )
        )