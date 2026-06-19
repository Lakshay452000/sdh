from fastapi import FastAPI

from app.routers.chat_router import router as chat_router
from app.exceptions.handlers import (
    register_exception_handlers
)
from app.routers.document_router import (
    router as document_router
)
from app.routers.interview_router import (
    router as interview_router
)
from app.routers.architecture_router import (
    router as architecture_router
)
from app.evaluation.controllers.evaluation_router import(
    router as evaluation_router
)
from app.agent.controllers.agent_controller import router as agent_router
from app.multi_agent.controllers.workflow_controller import (
    router as workflow_router
)
app = FastAPI()
app.include_router(chat_router)
app.include_router(document_router)
app.include_router(interview_router)
register_exception_handlers(app)
app.include_router(architecture_router)
app.include_router(evaluation_router)
app.include_router(agent_router)
app.include_router(
    workflow_router
)


@app.get("/")
def home():
    return {
        "message": "SDH is running"
    }