import functools
import math
import sys
from typing import Iterator, List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from utilities import MaxHeap, MinHeap


class Star:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs: 'Star') -> bool:
        return self.distance < rhs.distance

    def __repr__(self):
        return str(self.distance)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)


def find_closest_k_stars(stars: Iterator[Star], k: int) -> List[Star]:
    heap = MinHeap()
    for star in stars:
        heap += star

    result = []
    for _ in range(k):
        result.append(heap())

    return result


def find_closest_k_stars_optimal(stars: Iterator[Star], k: int) -> List[Star]:
    heap: MaxHeap[Star] = MaxHeap()

    for star in stars:
        if len(heap) < k:
            heap += star
        elif heap.peek() > star:
            heap()
            heap += star

    result = []

    for _ in range(k):
        result.append(heap())

    return result


def comp(expected_output, output):
    if len(output) != len(expected_output):
        return False
    return all(
        math.isclose(s.distance, d)
        for s, d in zip(sorted(output), expected_output))


@enable_executor_hook
def find_closest_k_stars_wrapper(executor, stars, k):
    stars = [Star(*a) for a in stars]
    return executor.run(functools.partial(find_closest_k_stars_optimal, iter(stars), k))


if __name__ == '__main__':
    sys.exit(
        generic_test.generic_test_main('k_closest_stars.py',
                                       'k_closest_stars.tsv',
                                       find_closest_k_stars_wrapper, comp))
