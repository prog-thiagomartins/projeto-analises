"""Models used for asking questions and returning answers."""

from datetime import datetime
from pydantic import BaseModel, Field

class Question(BaseModel):
    question: str

class Answer(BaseModel):
    answer: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
