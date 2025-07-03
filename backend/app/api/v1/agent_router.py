"""Routes for agent management and interaction."""

from fastapi import APIRouter, HTTPException, UploadFile, File

from ...models.agent import Agent, AgentCreate
from ...models.message import Question, Answer
from ...models.document import Document
from ...services.agent_service import AgentService

router = APIRouter()
service = AgentService()

@router.post("/", response_model=Agent)
def create_agent(agent_in: AgentCreate):
    return service.create_agent(agent_in)

@router.get("/", response_model=list[Agent])
def list_agents():
    return service.list_agents()

@router.get("/{agent_id}", response_model=Agent)
def get_agent(agent_id: str):
    agent = service.get_agent(agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent


@router.post("/{agent_id}/context", response_model=list[Document])
def upload_context(agent_id: str, files: list[UploadFile] = File(...)):
    try:
        docs = service.add_context(agent_id, files)
    except KeyError:
        raise HTTPException(status_code=404, detail="Agent not found")
    return docs

@router.post("/{agent_id}/ask", response_model=Answer)
def ask_agent(agent_id: str, question: Question):
    try:
        answer = service.ask_agent(agent_id, question.question)
    except KeyError:
        raise HTTPException(status_code=404, detail="Agent not found")
    return Answer(answer=answer)
