"""
TODO:

`foo` takes keyword arguments of type integer or string.
"""


def foo(**kwargs: int | str): ...


## Check types
foo(a=1, b="2")
foo(a=[1])  # type: ignore
