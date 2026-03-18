"""
TODO:

Define a decorator that wraps a function and returns a function with the same signature.
"""

from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T", bound=Callable)


def decorator(func: T) -> T:
    return func


## Check types
@decorator
def foo(a: int, *, b: str) -> None: ...


@decorator
def bar(c: int, d: str) -> None: ...


foo(1, b="2")
bar(c=1, d="2")

foo(1, "2")  # type: ignore
foo(a=1, e="2")  # type: ignore
decorator(1)  # type: ignore
