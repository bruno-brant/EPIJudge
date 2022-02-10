import math
from typing import List

from test_framework import generic_test


class MinHeap:
    data = []

    def __add__(self, item: int):
        self.data.append(item)

        i = len(self.data) - 1  # last item

        while i != 0 and item < self.data[self._parent(i)]:
            self._swap(i, self._parent(i))
            i = self._parent(i)

        return self

    def pop(self) -> int:
        """Extract min"""

        if len(self.data) == 1:
            return self.data.pop()

        min = self.data[0]

        self.data[0] = self.data.pop()
        self._min_heapify(0)

        return min

    def __len__(self):
        return len(self.data)

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return repr(self.data)

    def _parent(self, i):
        return math.floor((i - 1) / 2)

    def _left(self, i):
        return (i * 2) + 1

    def _right(self, i):
        return (i * 2) + 2

    def _min_heapify(self, i: int):
        heap_size = len(self.data)
        left_idx = self._left(i)
        right_idx = self._right(i)
        min_idx = i

        if left_idx < heap_size and self.data[left_idx] < self.data[min_idx]:
            min_idx = left_idx

        if right_idx < heap_size and self.data[right_idx] < self.data[min_idx]:
            min_idx = right_idx

        if i == min_idx:
            return

        self._swap(i, min_idx)
        self._min_heapify(min_idx)

    def _swap(self, idx_a, idx_b):
        temp = self.data[idx_a]
        self.data[idx_a] = self.data[idx_b]
        self.data[idx_b] = temp


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    def pop_one_from_each():
        remove = []
        for i, list in enumerate(sorted_arrays):
            yield list.pop(0)

            if not list:
                remove.append(i)

        for i in reversed(remove):
            sorted_arrays.pop(i)

    min_heap = MinHeap()
    while sorted_arrays:
        for item in pop_one_from_each():
            min_heap += item

    result = []
    while min_heap:
        result.append(min_heap.pop())

    return result


def test(arrs: list[list[int]]):
    expected = [item for sublist in arrs for item in sublist]
    expected = list(sorted(expected))
    actual = merge_sorted_arrays(arrs)

    assert actual == expected, f"Expected {expected}, got {actual}"


if __name__ == '__main__':
    test([])
    test([[1]])
    test([[1], [1]])
    test([[1, 3], [2], [0]])

    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
