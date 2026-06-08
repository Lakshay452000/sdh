from pydantic import (
    BaseModel,
    Field
)

from app.schemas.metadata_filter import (
    MetadataFilter
)


class AskRequest(BaseModel):

    session_id: str = Field(
        min_length=1,
        max_length=100
    )

    question: str = Field(
        min_length=3,
        max_length=500
    )

    metadata_filter: (
        MetadataFilter | None
) = None