"""Base classes for file parsing."""

from __future__ import annotations

from fastapi import UploadFile
from abc import ABC, abstractmethod
from typing import Any


class BaseParser(ABC):
    """Base parser interface."""

    @abstractmethod
    def parse(self, file: UploadFile) -> Any:
        """Parse an uploaded file and return structured content."""
        raise NotImplementedError
