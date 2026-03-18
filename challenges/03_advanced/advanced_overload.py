"""
TODO:
`process` is a function that takes one argument `response`
- When `response` is bytes, `process` returns a string
- When `response` is an integer, `process` returns tuple[int, str]
- When `response` is None, `process` returns None
"""

from typing import overload


@overload
def process(response: None) -> None: ...


@overload
def process(response: int) -> tuple[int, str]: ...


@overload
def process(response: bytes) -> str: ...


def process(response: int | bytes | None) -> str | None | tuple[int, str]: ...


## Check types
from typing import assert_type

assert_type(process(b"42"), str)
assert_type(process(42), tuple[int, str])
assert_type(process(None), None)

assert_type(process(42), str)  # type: ignore
assert_type(process(None), str)  # type: ignore
assert_type(process(b"42"), tuple[int, str])  # type: ignore
assert_type(process(None), tuple[int, str])  # type: ignore
assert_type(process(42), str)  # type: ignore
assert_type(process(None), str)  # type: ignore
