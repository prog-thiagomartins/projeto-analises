from __future__ import annotations

from pathlib import Path
from typing import Dict, List

from fastapi import UploadFile

from ..models.document import Document
from ..parsers.base_parser import BaseParser
from ..parsers.excel_parser import ExcelParser
from ..parsers.csv_parser import CSVParser
from ..parsers.pdf_parser import PDFParser


class DocumentService:
    """Service responsible for parsing and storing documents in memory."""

    def __init__(self) -> None:
        self.documents: Dict[str, Document] = {}
        self.parsers: Dict[str, BaseParser] = {
            ".xlsx": ExcelParser(),
            ".csv": CSVParser(),
            ".pdf": PDFParser(),
        }

    def _select_parser(self, suffix: str) -> BaseParser:
        """Return the parser responsible for a given file suffix."""
        parser = self.parsers.get(suffix)
        if not parser:
            raise ValueError(f"Unsupported file type: {suffix}")
        return parser

    def parse_file(self, file: UploadFile) -> Document:
        """Parse an uploaded file and store it as a Document."""
        suffix = Path(file.filename).suffix.lower()
        parser = self._select_parser(suffix)
        content = parser.parse(file)
        doc = Document(name=file.filename, content=content)
        self.documents[doc.id] = doc
        return doc

    def add_document(self, data: Document | DocumentCreate) -> Document:
        """Store a document created externally or from raw data."""
        if isinstance(data, Document):
            doc = data
        else:
            doc = Document.from_create(data)
        self.documents[doc.id] = doc
        return doc

    def list_documents(self) -> List[Document]:
        """Return all parsed documents."""
        return list(self.documents.values())

    def get_document(self, doc_id: str) -> Document | None:
        """Retrieve a single document by id."""
        return self.documents.get(doc_id)
