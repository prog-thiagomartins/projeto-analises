from __future__ import annotations

import pandas as pd
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
        df = pd.read_excel(file.file)
        return Table(df)
