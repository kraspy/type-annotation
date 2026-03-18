"""
TODO:

Make sure `my_list` cannot be re-assigned to.
"""

from typing import Final

my_list: Final = []

## Check types
my_list.append(1)
my_list = []  # type: ignore
my_list = "something else"  # type: ignore
