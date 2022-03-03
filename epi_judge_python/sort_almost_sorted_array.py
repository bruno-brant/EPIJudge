from typing import Iterator, List

from test_framework import generic_test
from utilities import MaxHeap, MinHeap


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    heap = MinHeap()

    while len(heap) != k:
        heap += next(sequence)

    result = []
    for remaining in sequence:
        result.append(heap())
        heap += remaining

    while heap:
        result.append(heap())

    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
