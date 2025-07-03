from fastapi import UploadFile
from io import BytesIO

from app.services.agent_service import AgentService
from app.models.agent import AgentCreate
from app.models.document import Document


def test_create_agent():
    service = AgentService()
    agent = service.create_agent(AgentCreate(name="Test", description="d", objective="o"))
    assert agent.name == "Test"
    assert agent.id in service.agents


def test_add_context(monkeypatch):
    service = AgentService()
    agent = service.create_agent(AgentCreate(name="A", description="d", objective="o"))

    async def fake_parse(file: UploadFile):
        return Document(name=file.filename, content="data")

    # monkeypatch the parse_file method to avoid external deps
    monkeypatch.setattr(service.doc_service, "parse_file", fake_parse)

    upload = UploadFile(filename="test.txt", file=BytesIO(b"demo"))
    docs = service.add_context(agent.id, [upload])
    assert docs[0].name == "test.txt"
    assert docs[0].id in service.doc_service.documents


def test_ask_agent():
    service = AgentService()
    agent = service.create_agent(AgentCreate(name="A", description="d", objective="o"))
    # simulate context
    service.contexts[agent.id] = [Document(name="doc", content=None)]
    answer = service.ask_agent(agent.id, "ola")
    assert "ola" in answer

