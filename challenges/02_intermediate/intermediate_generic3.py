"""
TODO:

The function `add` accepts one argument and returns a value, they all have the same type.
The type can only be int or subclasses of int.
"""

from typing import TypeVar, assert_type

T = TypeVar("T", bound=int)


def add(a: T) -> T: ...


## Check types
class MyInt(int):
    pass


assert_type(add(1), int)
assert_type(add(MyInt(1)), MyInt)
assert_type(add("1"), str)  # type: ignore
add(["1"], ["2"])  # type: ignore
add("1", 2)  # type: ignore
