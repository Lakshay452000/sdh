from fastapi import (
    APIRouter
)

from app.dependencies.workflow_dependencies import (
    workflow_service
)
from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form
)

router = APIRouter(
    prefix="/workflow",
    tags=["Workflow"]
)


@router.get("/test")
async def test():

    result = await (
        workflow_service.execute(
            architecture_description=
                "Netflix architecture",

            image_bytes=b"test"
        )
    )

    return result

@router.post(
    "/review"
)
async def review_workflow(
    architecture_description: str = Form(...),
    diagram: UploadFile = File(...)
):

    image_bytes = await (
        diagram.read()
    )

    result = await (
        workflow_service.execute(
            architecture_description=
                architecture_description,

            image_bytes=
                image_bytes
        )
    )

    return {
        "review":
            result["review"],

        "evaluation":
            result["evaluation"],

        "correction":
            result["correction"],

        "verification":
            result["verification"],

        "mermaid_diagram":
            result["mermaid_diagram"]
    }