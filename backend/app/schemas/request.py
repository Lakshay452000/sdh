from pydantic import (
    BaseModel,
    Field
)

from app.schemas.metadata_filter import (
    MetadataFilter
)


class AskRequest(BaseModel):

    question: str = Field(
        min_length=3,
        max_length=500
    )

    metadata_filter: (
        MetadataFilter | None
    ) = None