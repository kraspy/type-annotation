"""
TODO:

The function `add` accepts two arguments and returns a value, they all have the same type.
The type can only be str or int.
"""

from typing import TypeVar, assert_type

T = TypeVar("T", int, str)


def add(a: T, b: T) -> T: ...


## Check types
assert_type(add(1, 2), int)
assert_type(add("1", "2"), str)

add(["1"], ["2"])  # type: ignore
add("1", 2)  # type: ignore
