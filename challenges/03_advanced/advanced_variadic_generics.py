"""
TODO:

Define an `Array` type that supports element-wise addition of arrays
with identical dimensions and types.
"""

from typing import Generic, TypeVarTuple, Unpack

Ts = TypeVarTuple("Ts")


class Array(Generic[Unpack[Ts]]):
    def __add__(self, other: "Array[Unpack[Ts]]") -> "Array[Unpack[Ts]]": ...


## Check types
from typing import assert_type

a: Array[float, int] = Array()
b: Array[float, int] = Array()
assert_type(a + b, Array[float, int])

c: Array[float, int, str] = Array()
assert_type(a + c, Array[float, int, str])  # type: ignore
