from pydantic import (
    BaseModel,
    Field
)

from app.schemas.chat_role import (
    ChatRole
)


class ChatMessage(BaseModel):
    role: ChatRole

    content: str = Field(
        min_length=1
    )