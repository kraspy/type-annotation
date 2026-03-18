def foo(x: int | None = 0):
    pass


## Check types
foo(10)
foo(None)
foo()

foo("10")  # type: ignore
