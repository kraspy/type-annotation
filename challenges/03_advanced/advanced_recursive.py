"""
TODO:

Define a `Tree` type. `Tree` is a dictionary, whose keys are string, values are also `Tree`.
"""

from typing import Dict, TypeAlias

Tree: TypeAlias = Dict[str, "Tree"]


## Check types
def f(t: Tree) -> None:
    pass


f({})
f({"foo": {}})
f({"foo": {"bar": {}}})
f({"foo": {"bar": {"baz": {}}}})


f(1)  # type: ignore
f({"foo": []})  # type: ignore
f({"foo": {1: {}}})  # type: ignore
