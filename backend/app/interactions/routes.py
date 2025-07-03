"""Example interaction routes using the legacy agent storage."""

from fastapi import APIRouter, HTTPException

from ..agents.routes import AGENTS
from ..agents.models import Agent

router = APIRouter()

@router.post("/{agent_id}/ask")
def ask_agent(agent_id: str, question: str):
    agent: Agent | None = AGENTS.get(agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    # Mock response; integration with Docling + CrewAI would go here
    answer = f"Agent {agent.name} responds to '{question}' with insights from documents."
    return {"answer": answer}
