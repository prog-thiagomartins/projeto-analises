"""Excel parser that converts sheets to Docling tables."""

from __future__ import annotations

try:
    import pandas as pd  # type: ignore
except Exception:  # pragma: no cover - pandas may not be installed
    pd = None  # type: ignore
from fastapi import UploadFile
from typing import Any

from .base_parser import BaseParser

try:
    from docling import Table
except Exception:  # pragma: no cover - Docling may not be installed
    class Table:  # type: ignore
        def __init__(self, data: Any) -> None:
            self.data = data

        def __repr__(self) -> str:  # pragma: no cover - simple representation
            return f"Table(rows={len(self.data)})"


class ExcelParser(BaseParser):
    """Parse .xlsx files into Docling Table structures."""

    def parse(self, file: UploadFile) -> Any:
        if pd is None:  # pragma: no cover - handled when pandas is unavailable
            raise RuntimeError("pandas is required to parse Excel files")
        df = pd.read_excel(file.file)
        return Table(df)
