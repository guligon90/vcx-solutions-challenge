# Base imports
from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Optional, TypeVar


T = TypeVar('T')


@dataclass
class Cell(Generic[T]):
    item: Optional[T] = None
    next: Optional[Cell] = None
