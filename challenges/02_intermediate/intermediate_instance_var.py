"""
TODO:

Class `Foo` has an instance variable `bar`, which is an integer.
"""


class Foo:
    bar: int


## Check types
foo = Foo()
foo.bar = 1
foo.bar = "1"  # type: ignore
