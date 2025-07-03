from __future__ import annotations
from typing import Dict, List

from ..models.agent import Agent, AgentCreate

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

    def create_agent(self, data: AgentCreate) -> Agent:
        agent = Agent.from_create(data)
        self.agents[agent.id] = agent
        return agent

    def list_agents(self) -> List[Agent]:
        return list(self.agents.values())

    def get_agent(self, agent_id: str) -> Agent | None:
        return self.agents.get(agent_id)

    def ask_agent(self, agent_id: str, question: str) -> str:
        agent = self.get_agent(agent_id)
        if not agent:
            raise KeyError("Agent not found")

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

        # Fallback simulated response
        return f"Agente '{agent.name}' responde de acordo com o objetivo '{agent.objective}'. Pergunta: '{question}'"
