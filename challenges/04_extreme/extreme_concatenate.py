"""
TODO:

Suppose there's a function `foo`, whose first parameter can be anything.

You want to use `foo`, but want to restrict the first argument to be a `Person`.
You cannot modify `foo`, so you decide to write a function `transform`,
to transform `foo` into the function you want.
"""

from typing import Any, Callable, Concatenate, ParamSpec, TypeVar

T = TypeVar("T")
P = ParamSpec("P")


class Person:
    pass


def transform(
    f: Callable[Concatenate[Any, P], T],
) -> Callable[Concatenate[Person, P], T]:
    def wrapper(value: Person, /, *args: P.args, **kwargs: P.kwargs) -> T:
        return f(value, *args, **kwargs)

    return wrapper


## Check types
def foo(value: Any, mode: str) -> None:
    pass


foo_with_person = transform(foo)
foo_with_person(Person(), "1")
foo_with_person(Person(), mode="1")
foo_with_person(1, "1")  # type: ignore[arg-type]
foo_with_person(Person(), 1)  # type: ignore[arg-type]
foo_with_person(Person(), "1", 2)  # type: ignore[call-arg]


def foo2(value: Any, mode: str, *, maybe: bool) -> int:
    return 1


foo_with_person2 = transform(foo2)
foo_with_person2(Person(), "1", maybe=True)
foo_with_person2(Person(), mode="1", maybe=True)
foo_with_person2(Person(), mode="1")  # type: ignore[call-arg]
foo_with_person2(Person(), 1, maybe=True)  # type: ignore[arg-type]
foo_with_person2(Person(), "1", maybe=1)  # type: ignore[arg-type]
foo_with_person2(Person(), "1", True)  # type: ignore[misc]
