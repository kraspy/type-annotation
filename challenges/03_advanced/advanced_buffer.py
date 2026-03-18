"""
TODO:

Annotate the function `read_buffer`, which accepts anything that is a buffer.

See https://docs.python.org/3.12/reference/datamodel.html#object.__buffer__
"""

from collections.abc import Buffer


def read_buffer(b: Buffer) -> None: ...


## Check types

from array import array


class MyBuffer:
    def __init__(self, data: bytes) -> None:
        self.data = bytearray(data)
        self.view: memoryview | None = None

    def __buffer__(self, flags: int) -> memoryview:
        self.view = memoryview(self.data)
        return self.view


read_buffer(b"foo")
read_buffer(memoryview(b"foo"))
read_buffer(array("l", [1, 2, 3, 4, 5]))
read_buffer(MyBuffer(b"foo"))
read_buffer("foo")  # type: ignore[arg-type]
read_buffer(1)  # type: ignore[arg-type]
read_buffer(["foo"])  # type: ignore[arg-type]
