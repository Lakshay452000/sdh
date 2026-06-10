from app.interview.model.interview_session import (
    InterviewSession
)
from app.interview.model.interview_stage import (
    InterviewStage
)


from app.interview.model.interview_stage import (
    InterviewStage
)


class InterviewStageManager:

    STAGE_ORDER = [
        InterviewStage.REQUIREMENTS,
        InterviewStage.CAPACITY_ESTIMATION,
        InterviewStage.HIGH_LEVEL_DESIGN,
        InterviewStage.DEEP_DIVE,
        InterviewStage.BOTTLENECKS,
        InterviewStage.FINAL_REVIEW
    ]

    STAGE_MESSAGE_LIMITS = {
        InterviewStage.REQUIREMENTS: 2,
        InterviewStage.CAPACITY_ESTIMATION: 2,
        InterviewStage.HIGH_LEVEL_DESIGN: 2,
        InterviewStage.DEEP_DIVE: 2,
        InterviewStage.BOTTLENECKS: 2
    }

    def advance_stage_if_needed(
        self,
        session: InterviewSession
    ) -> None:

        current_stage = session.current_stage

        limit = self.STAGE_MESSAGE_LIMITS.get(
            current_stage
        )

        if limit is None:
            return

        if session.stage_message_count < limit:
            return

        current_index = self.STAGE_ORDER.index(
            current_stage
        )
        session.stage_message_count = 0
        if current_index < len(self.STAGE_ORDER) - 1:
            session.current_stage = (
                self.STAGE_ORDER[
                    current_index + 1
                ]
            )