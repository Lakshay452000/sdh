from fastapi import APIRouter
from fastapi import Depends

from app.agent.schemas.agent_request import AgentRequest
from app.agent.schemas.agent_response import AgentResponse

from app.agent.services.agent_service import AgentService
from app.dependencies.agent_dependencies import get_agent_service

router = APIRouter(prefix="/agent", tags=["Agent"])


@router.post("/chat", response_model=AgentResponse)
def chat(
    request: AgentRequest,
    agent_service: AgentService = Depends(get_agent_service)
):

    response = agent_service.chat(request.query)

    return AgentResponse(response=response)