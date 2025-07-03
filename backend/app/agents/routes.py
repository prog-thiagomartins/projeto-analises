"""Legacy agent routes kept for reference."""

from fastapi import APIRouter, HTTPException

from .models import Agent, AgentCreate

router = APIRouter()

AGENTS: dict[str, Agent] = {}

@router.post("/", response_model=Agent)
def create_agent(agent_in: AgentCreate):
    agent = Agent.from_create(agent_in)
    AGENTS[agent.id] = agent
    return agent

@router.get("/", response_model=list[Agent])
def list_agents():
    return list(AGENTS.values())

@router.get("/{agent_id}", response_model=Agent)
def get_agent(agent_id: str):
    agent = AGENTS.get(agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent
