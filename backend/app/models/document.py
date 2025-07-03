from __future__ import annotations
from pydantic import BaseModel, Field
from uuid import uuid4
from typing import Any

class DocumentCreate(BaseModel):
    name: str
    content: Any = None

class Document(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    content: Any = None

    @classmethod
    def from_create(cls, data: DocumentCreate) -> "Document":
        return cls(**data.dict())
