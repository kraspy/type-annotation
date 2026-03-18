"""
TODO:

Create a new type called Vector, which is a list of float.
"""

from typing import TypeAlias

Vector: TypeAlias = list[float]


## Check types
def foo(v: Vector) -> None: ...


foo([1.1, 2])
foo(1)  # type: ignore
foo(["1"])  # type: ignore
