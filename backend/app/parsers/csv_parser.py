"""CSV parser returning Docling tables."""

from __future__ import annotations

import pandas as pd
from fastapi import UploadFile
from typing import Any

from .base_parser import BaseParser

try:
    from docling import Table
except Exception:  # pragma: no cover
    class Table:  # type: ignore
        def __init__(self, data: Any) -> None:
            self.data = data

        def __repr__(self) -> str:
            return f"Table(rows={len(self.data)})"


class CSVParser(BaseParser):
    """Parse .csv files into Docling Table structures."""

    def parse(self, file: UploadFile) -> Any:
        df = pd.read_csv(file.file)
        return Table(df)
