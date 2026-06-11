from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.exceptions.interview_session_not_found_exception import (
    InterviewSessionNotFoundException
)
from app.exceptions.invalid_diagram_exception import (
    InvalidDiagramException
)

from app.exceptions.diagram_analysis_exception import (
    DiagramAnalysisException
)

def register_exception_handlers(app: FastAPI):

    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Request,
        exc: Exception
    ):
        return JSONResponse(
            status_code=500,
            content={
                "message": "Internal Server Error"
            }
        )
    
    @app.exception_handler(
        InterviewSessionNotFoundException
    )
    async def interview_session_not_found_handler(
        request: Request,
        exc: InterviewSessionNotFoundException
    ):
        return JSONResponse(
            status_code=404,
            content={
                "message": str(exc)
            }
        )
    
    @app.exception_handler(
        InvalidDiagramException
    )
    async def invalid_diagram_handler(
        request: Request,
        exc: InvalidDiagramException
    ):
        return JSONResponse(
            status_code=400,
            content={
                "message": str(exc)
            }
        )
    
    @app.exception_handler(
        DiagramAnalysisException
    )
    async def diagram_analysis_handler(
        request: Request,
        exc: DiagramAnalysisException
    ):
        return JSONResponse(
            status_code=500,
            content={
                "message": str(exc)
            }
        )