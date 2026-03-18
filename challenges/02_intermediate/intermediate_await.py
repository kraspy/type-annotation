"""
TODO:

`run_async` takes an awaitable integer.
"""

from asyncio import Queue
from collections.abc import Awaitable


def run_async(func: Awaitable[int]): ...


## Check types
queue: Queue[int] = Queue()
queue2: Queue[str] = Queue()


async def async_function() -> int:
    return await queue.get()


async def async_function2() -> str:
    return await queue2.get()


run_async(async_function())
run_async(1)  # type: ignore
run_async(async_function2())  # type: ignore
