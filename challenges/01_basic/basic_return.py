def foo() -> int:
    return 1


## Check types
from typing import assert_type

assert_type(foo(), int)
assert_type(foo(), str)  # type: ignore
