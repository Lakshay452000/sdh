from pydantic import BaseModel


class MetadataFilter(BaseModel):

    document_id: str | None = None

    file_name: str | None = None

    level: int | None = None

    chunk_type: str | None = None