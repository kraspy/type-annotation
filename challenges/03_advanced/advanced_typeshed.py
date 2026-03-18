"""
TODO:

Annotate class `MyContainer`, which should support item access, i.e.
using `[x]` to get, set, and delete an item.

HINT: Use https://github.com/python/typeshed/blob/main/stdlib/_typeshed/__init__.pyi
"""

from _typeshed import SupportsItemAccess


class MyContainer(SupportsItemAccess): ...


## Check types
from collections.abc import Mapping
from typing import assert_type

c = MyContainer()
c[1] = 1
c["2"] = 2
print(c[1])
print(c["2"])
del c[1]
del c["2"]
assert_type(c, dict)  # type: ignore
assert_type(c, Mapping)  # type: ignore
