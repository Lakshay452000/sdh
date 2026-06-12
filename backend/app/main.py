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
app = FastAPI()
app.include_router(chat_router)
app.include_router(document_router)
app.include_router(interview_router)
register_exception_handlers(app)
app.include_router(architecture_router)


@app.get("/")
def home():
    return {
        "message": "SDH is running"
    }