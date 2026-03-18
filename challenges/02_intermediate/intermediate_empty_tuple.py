"""
TODO:

foo should accept a empty tuple argument.
"""


def foo(x: tuple[()]):
    pass


## Check types
foo(())
foo((1,))  # type: ignore
