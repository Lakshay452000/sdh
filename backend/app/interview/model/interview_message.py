from datetime import datetime

from pydantic import BaseModel


class InterviewMessage(BaseModel):
    role: str
    content: str
    timestamp: datetime