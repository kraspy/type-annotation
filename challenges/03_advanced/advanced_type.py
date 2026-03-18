"""
TODO:

`make_object` takes a class returns an instance of it.
"""

from typing import TypeVar

T = TypeVar("T")


def make_object(cls: type[T]) -> T: ...


## Check types
from typing import assert_type


class MyClass:
    pass


def f() -> None:
    pass


assert_type(make_object(MyClass), MyClass)
assert_type(make_object(int), int)

make_object(f)  # type: ignore
make_object("sss")  # type: ignore
make_object(["sss"])  # type: ignore
