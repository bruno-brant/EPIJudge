from heapq import merge
from typing import List

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    for list in sorted_arrays:
        list.reverse()

    top = [arr.pop() if arr else None for arr in sorted_arrays]

    result = []

    while any(sorted_arrays) or any(map(lambda x: x != None, top)):
        min_idx = -1
        for i in range(0, len(top)):
            if top[i] == None:
                continue

            if min_idx == -1:
                min_idx = i
            elif top[i] < top[min_idx]:
                min_idx = i

        result.append(top[min_idx])

        top[min_idx] = sorted_arrays[min_idx].pop() if sorted_arrays[min_idx] else None 

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
