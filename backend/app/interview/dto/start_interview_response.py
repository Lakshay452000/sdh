from pydantic import BaseModel


class StartInterviewResponse(BaseModel):
    session_id: str
    first_question: str