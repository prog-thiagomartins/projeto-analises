from __future__ import annotations
from typing import Dict, List

from ..models.document import Document, DocumentCreate

class DoclingParser:
    """Placeholder for Docling integration."""

    def parse(self, content: str) -> str:
        # In real scenario this would parse the content using Docling
        return content


class DocumentService:
    def __init__(self) -> None:
        self.documents: Dict[str, Document] = {}
        self.parser = DoclingParser()

    def add_document(self, data: DocumentCreate) -> Document:
        doc = Document.from_create(data)
        # Mock parsing step
        doc.content = self.parser.parse(doc.content)
        self.documents[doc.id] = doc
        return doc

    def list_documents(self) -> List[Document]:
        return list(self.documents.values())

    def get_document(self, doc_id: str) -> Document | None:
        return self.documents.get(doc_id)
