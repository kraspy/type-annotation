"""
TODO:

foo should accept a argument that's either a string or integer.
"""


def foo(x: str | int) -> None:
    pass


## Check types
foo("foo")
foo(1)

foo([])  # type: ignore
