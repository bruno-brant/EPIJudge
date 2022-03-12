from ast import With
import collections
import functools
import sys
from typing import Dict, List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


class Knapsack:
    def __init__(self, items: List[Item] = None) -> None:
        if items:
            self._items = items
            self._weight = sum(map(lambda i: i.weight,  items))
            self._value = sum(map(lambda i: i.value,  items))

    def __add__(self, item: Item) -> 'Knapsack':
        r = Knapsack()
        r._items = self._items + [item]
        r._weight = self._weight + item.weight
        r._value = self._value + item.value

        return r

    def __str__(self) -> str:
        return f"{self.value}/{self.weight}"

    def __repr__(self) -> str:
        return str(self)

    @property
    def value(self):
        return self._value

    @property
    def weight(self):
        return self._weight


global_cache = {}


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    return enumerate_knapsacks(items, capacity, {})


def enumerate_knapsacks(items: List[Item], capacity: int, cache: Dict) -> List[Knapsack]:
    if capacity <= 0 or len(items) == 0:
        return 0

    cache_key = (len(items), capacity)
    cached = cache.get(cache_key, None)

    if cached:
        return cached

    current = items[0]

    if len(items) == 1 and current.weight <= capacity:
        return current.value

    value = enumerate_knapsacks(items[1:], capacity, cache)

    if current.weight <= capacity:
        with_current = current.value + \
            enumerate_knapsacks(items[1:], capacity - current.weight, cache)
        if with_current > value:
            value = with_current

    cache[cache_key] = value

    return value


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


def test(items, expected):
    actual = optimum_subject_to_capacity(
        [Item(i[1], i[0]) for i in items], 130)
    assert actual == expected, f"Expected {expected}, got {actual}"


if __name__ == '__main__':
    clocks = [
        (65, 20), (35, 8), (245, 60), (195, 55), (65, 40), (150, 70), (275, 85),
        (155, 25), (120, 30), (320, 65), (75, 75), (40, 10), (200, 95), (100, 50),
        (200, 95), (100, 50), (220, 40), (99, 10)
    ]

    test(clocks, 695)

    sys.exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
