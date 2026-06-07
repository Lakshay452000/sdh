from pydantic import BaseModel


class HierarchyNode(BaseModel):
    node_id: str
    parent_id: str | None
    level: int
    text: str
    document_id: str
    children_count: int = 0