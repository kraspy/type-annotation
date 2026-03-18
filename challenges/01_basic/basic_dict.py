def foo(x: dict[str, str]):
    pass


## Check types
foo({"foo": "bar"})
foo({"foo": 1})  # type: ignore
