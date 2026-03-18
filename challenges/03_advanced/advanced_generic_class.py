"""
TODO:

Define a generic class that represents a stack.
It can be instantiated with a certain type, with method `push` accepting an object of the specified type,
and `pop` returning an an object of the same type
"""

from typing import Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()


## Check types
from typing import assert_type

s = Stack[int]()
s.push(1)
assert_type(s.pop(), int)
s.push("foo")  # type: ignore
assert_type(s.pop(), str)  # type: ignore
