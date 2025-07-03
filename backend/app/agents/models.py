from pydantic import BaseModel
from uuid import uuid4

class AgentCreate(BaseModel):
    name: str
    description: str
    goals: list[str]

class Agent(BaseModel):
    id: str
    name: str
    description: str
    goals: list[str]

    @classmethod
    def from_create(cls, data: AgentCreate) -> "Agent":
        return cls(id=str(uuid4()), **data.dict())
