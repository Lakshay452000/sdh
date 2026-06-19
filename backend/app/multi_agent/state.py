from typing import TypedDict


class ArchitectureWorkflowState(
    TypedDict,
    total=False
):

    architecture_description: str

    image_bytes: bytes

    review: object

    evaluation: object

    correction: object

    verification: str
    mermaid_diagram: str