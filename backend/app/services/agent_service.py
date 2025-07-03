from __future__ import annotations
from typing import Dict, List

from fastapi import UploadFile

from ..models.agent import Agent, AgentCreate
from ..models.document import Document
from .document_service import DocumentService

try:
    from crewai import Agent as CrewAgent, Task, Crew
    from langchain.tools import tool
except Exception:  # pragma: no cover - library might not be installed
    CrewAgent = None
    Task = None
    Crew = None
    tool = None


class AgentService:
    """Service layer for managing agents and questions."""

    def __init__(self) -> None:
        self.agents: Dict[str, Agent] = {}
        self.contexts: Dict[str, List[Document]] = {}
        self.doc_service = DocumentService()

    def create_agent(self, data: AgentCreate) -> Agent:
        """Instantiate and register a new agent."""
        agent = Agent.from_create(data)
        self.agents[agent.id] = agent
        self.contexts[agent.id] = []
        return agent

    def list_agents(self) -> List[Agent]:
        """Return all registered agents."""
        return list(self.agents.values())

    def get_agent(self, agent_id: str) -> Agent | None:
        """Retrieve a single agent by id."""
        return self.agents.get(agent_id)

    def add_context(self, agent_id: str, files: List[UploadFile]) -> List[Document]:
        """Attach uploaded files as context to an agent."""
        agent = self.get_agent(agent_id)
        if not agent:
            raise KeyError("Agent not found")

        docs = [self.doc_service.parse_file(f) for f in files]
        self.contexts.setdefault(agent_id, []).extend(docs)
        agent.context_docs.extend([d.id for d in docs])
        agent.context_files.extend([d.name for d in docs])
        return docs

    def ask_agent(self, agent_id: str, question: str) -> str:
        """Return the agent answer for a given question."""
        agent = self.get_agent(agent_id)
        if not agent:
            raise KeyError("Agent not found")

        docs = self.contexts.get(agent_id, [])
        context_names = ", ".join(d.name for d in docs) if docs else "sem contexto"

        # Basic CrewAI integration example
        if CrewAgent and tool:
            @tool
            def mock_tool(q: str) -> str:
                return f"Resposta mock para '{q}'"

            crew_agent = CrewAgent(
                role=agent.name,
                goal=agent.objective,
                backstory=agent.description,
                tools=[mock_tool],
            )
            task = Task(description=question, expected_output="answer")
            crew = Crew(agents=[crew_agent], tasks=[task])
            try:
                result = crew.kickoff()
                return result
            except Exception:
                pass

        # Fallback simulated response using uploaded context
        return (
            f"Agente '{agent.name}' responde com base em {context_names}. "
            f"Pergunta: '{question}'"
        )
