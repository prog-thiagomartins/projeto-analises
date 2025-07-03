"""Pydantic models representing agents and their creation payloads."""

from __future__ import annotations
from pydantic import BaseModel, Field
from typing import List
from uuid import uuid4

class AgentCreate(BaseModel):
    name: str
    description: str
    objective: str
    context_files: List[str] = []

class Agent(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    description: str
    objective: str
    context_files: List[str] = []
    context_docs: List[str] = []

    @classmethod
    def from_create(cls, data: AgentCreate) -> "Agent":
        return cls(**data.dict())
