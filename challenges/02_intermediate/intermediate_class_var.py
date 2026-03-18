"""
TODO:

Class `Foo` has a class variable `bar`, which is an integer.
"""

from typing import ClassVar


class Foo:
    bar: ClassVar[int]
    """Hint: No need to write __init__"""


## Check types
Foo.bar = 1
Foo.bar = "1"  # type: ignore
Foo().bar = 1  # type: ignore
