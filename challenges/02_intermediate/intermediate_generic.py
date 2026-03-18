"""
TODO:

The function `add` accepts two arguments and returns a value, they all have the same type.
"""

from typing import List, TypeVar, assert_type

T = TypeVar("T")


def add(a: T, b: T) -> T: ...


## Check types
assert_type(add(1, 2), int)
assert_type(add("1", "2"), str)
assert_type(add(["1"], ["2"]), List[str])
assert_type(add(1, "2"), int)  # type: ignore
