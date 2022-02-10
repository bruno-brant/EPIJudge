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
        return i * 2

    def _right(self, i):
        return (i * 2) + 1

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
    result = []
    while sorted_arrays:
        for item in pop_one_from_each():
            min_heap += item

        result.append(min_heap.pop())

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

    sample = [[-20, -7, -6, -5, -2, 1, 3, 10, 11, 16], [-21, -19, -18, -13, -13, -12, -3, -2, 1, 3, 3, 6, 21], [-22, -15, -13, -12, -12, -6, -2, 0, 0, 4, 5, 7, 9, 10, 13, 13, 17, 17, 23, 23, 24, 24], [-24, -17, -10, -10, -6, -6, -3, -1, 0, 9, 15, 21, 22, 24], [-17, -17, -12, -11, -9, -8, -4, -4, 2, 5, 9, 17], [-21, -20, -9,
                                                                                                                                                                                                                                                                                                                        9, 14, 21, 23], [-22, -12, -10, -3, 5, 9, 16, 22, 24], [-21, -19, -17, -13, -12, -11, -9, -9, -4, 0, 0, 1, 1, 5, 7, 8, 8, 11, 15, 16, 19, 24], [-24, -4, -3, 1, 2, 3, 8, 12, 12], [-6, 13, 15, 17, 18], [-24, 4, 7, 10, 15], [-23, -10, -9, 5, 6, 6, 13, 16, 23], [-13, -5, -1, 0, 2, 7, 7, 9, 11, 13, 24], [-23, -20, -18, -10, -8, -5, -3, -2, -1, 2, 2, 4, 6, 8, 12, 13, 17], [-24, -24, -21, -19, -8, -3, 0, 2, 5, 6, 11, 17, 18, 20, 21], [-18, -16, -14, -13, -9, -8, -7, -5, 0, 0, 4, 4, 5, 8, 8, 9, 24], [-17, -12, -6, -2], [-24, -19, -19, -17, -12, -12, -11, -10, -9, -8, -7, -4, -3, 1, 3, 7, 8, 9, 10, 11, 16, 18, 21], [-14, -3, 1, 16, 24], [-23, -21, -19, -18, -17, -17, -14,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     -13, -8, -6, 0, 2, 5, 12, 12, 22, 23, 23], [-22, -20, -9, -5, -1, 4, 7, 12, 18, 22], [-23, -18, -17, -16, -15, 1, 4, 14, 16, 18, 19, 21, 23, 24], [-24, -22, -21, -21, -20, -15, -13, -9, -6, -4, 0, 0, 1, 5, 5, 6, 6, 8, 12, 13, 14, 17, 19], [-22, -19, 1]]

    test(sample)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
