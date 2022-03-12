import collections
import functools
import sys
from typing import List

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
    all_knapsacks = enumerate_knapsacks(items, capacity)

    return max(all_knapsacks, key=lambda item: item.value).value


def enumerate_knapsacks(items: List[Item], capacity: int) -> List[Knapsack]:
    if not items:
        return []

    previous_items = enumerate_knapsacks(items[1:], capacity)
    expanded_items = []
    current_item = items[0]

    for knapsack in previous_items:
        if (knapsack.weight + current_item.weight) <= capacity:
            expanded_items.append(knapsack + current_item)

    total = previous_items + expanded_items + [Knapsack([current_item])]

    return [item for item in total if item.weight <= capacity]


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


def test(items, expected):
    actual = optimum_subject_to_capacity([Item(i[1], i[0]) for i in items], 130)
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
