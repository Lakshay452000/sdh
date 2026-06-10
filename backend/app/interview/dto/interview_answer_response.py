from pydantic import BaseModel
from app.interview.model.interview_evaluation import (
    InterviewEvaluation
)



class InterviewAnswerResponse(BaseModel):
    next_question: str
    current_stage: str
    evaluation: InterviewEvaluation