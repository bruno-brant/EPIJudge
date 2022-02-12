from typing import Iterable


def cross(__iter1: Iterable, __iter2: Iterable):
    """Cross join of multiple Iterables"""

    for i in __iter1:
        for j in __iter2:
            yield (i, j)
