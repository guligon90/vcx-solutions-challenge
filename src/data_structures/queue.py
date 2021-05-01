# Base imports
from __future__ import annotations
from typing import Generic, Iterable, Optional, Union

# Project imports
from src.data_structures.common import Cell, T
from src.data_structures.exceptions import QueueDequeueException


class Queue(Generic[T]):

    def __init__(self, initial_queue: Union[T, Iterable[T]] = None) -> None:
        """Initializing queue."""
        self._length: int = 0
        self.head: Optional[Cell] = Cell()
        self.tail: Cell = self.head
        self.head.next = None

        if initial_queue:
            if isinstance(initial_queue, (list, tuple)):
                for value in initial_queue:
                    self.enqueue(value)
            else:
                self.enqueue(initial_queue)

    def enqueue(self, data: Union[T, Iterable[T]]) -> None:
        """Adds an element in the queue."""
        self.tail.next = Cell()
        self.tail = self.tail.next
        self.tail.item = data
        self.tail.next = None
        self._length += 1

    def dequeue(self) -> Optional[T]:
        """Removes an element of the queue."""
        data: Optional[T] = None

        if self.is_empty():
            raise QueueDequeueException()

        if self.head:
            self.head = self.head.next
            data = self.head.item if self.head else data
            self._length -= 1

        return data

    def is_empty(self) -> bool:
        """Verifies if the queue is empty."""
        return self.tail == self.head

    @staticmethod
    def print(queue: Queue) -> str:
        """Return string representation of a queue."""
        as_string: str = ''

        if queue.is_empty():
            return as_string

        while True:
            try:
                dequeued: Optional[T] = queue.dequeue()
                as_string += f'{str(dequeued)} -> '
            except QueueDequeueException:
                break

        return as_string[:-4]

    def __len__(self) -> int:
        """Returns the length of the queue."""
        return self._length

    def __repr__(self) -> str:
        """Queue representation will be a string."""
        return Queue.print(self)

    def __str__(self) -> str:
        """Queue representation will be a string."""
        return Queue.print(self)
