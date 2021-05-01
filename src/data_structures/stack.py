# Base imports
from __future__ import annotations
from typing import Generic, Iterable, Optional, Union

# Project imports
from src.data_structures.common import Cell, T
from src.data_structures.exceptions import StackPopException


class Stack(Generic[T]):

    """Singly linked list implementation of a stack (LIFO) data structure."""

    def __init__(self, initial_stack: Union[T, Iterable[T]] = None) -> None:
        """Initializing stack with a initial valid Iterable[T] or T, if informed."""
        self._length: int = 0
        self.head: Optional[Cell] = None

        if initial_stack:
            if isinstance(initial_stack, (list, tuple)):
                for value in initial_stack:
                    self.push(value)
            else:
                self.push(initial_stack)

    def push(self, data: Union[T, Iterable[T]]) -> None:
        """Pushes a generic data into the stack."""
        aux: Optional[Cell] = self.head
        self.head = Cell()
        self.head.item = data
        self.head.next = aux
        self._length += 1

    def pop(self) -> Optional[T]:
        """Pops a generic data out of the stack."""
        if self.is_empty():
            raise StackPopException()

        data: Optional[T] = None

        if self.head:
            data = self.head.item
            self.head = self.head.next
            self._length -= 1

        return data

    def is_empty(self) -> bool:
        """Indicates if the stack is empty."""
        return self.head is None

    @staticmethod
    def print(stack: Stack) -> str:
        """String representation of the stack."""
        current: Optional[Cell] = stack.head
        as_string: str = ''

        while current:
            as_string += f'{str(current.item)} -> '
            current = current.next

        return as_string[:-4]

    def __len__(self) -> int:
        """Returns the stack's length."""
        return self._length

    def __repr__(self) -> str:
        """Stack representation is a string."""
        return Stack.print(self)

    def __str__(self) -> str:
        """Stack representation is a string."""
        return Stack.print(self)
