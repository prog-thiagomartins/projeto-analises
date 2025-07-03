"""PDF parser that extracts text and splits pages."""

from __future__ import annotations

from fastapi import UploadFile
from typing import Any, List

from .base_parser import BaseParser

try:
    from docling import Text
except Exception:  # pragma: no cover
    class Text:  # type: ignore
        def __init__(self, content: str) -> None:
            self.content = content

        def __repr__(self) -> str:
            return f"Text(len={len(self.content)})"


class PDFParser(BaseParser):
    """Parse .pdf files splitting content by pages."""

    def parse(self, file: UploadFile) -> Any:
        try:
            from pdfminer.high_level import extract_text
        except Exception:
            # Fallback if pdfminer is not available
            text = file.file.read().decode("utf-8", errors="ignore")
        else:
            text = extract_text(file.file)
        pages = [Text(p.strip()) for p in text.split("\f") if p.strip()]
        return pages
