from cmath import exp
import sys
from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    if A is None:
        return []

    if len(A) == 1:
        return [A]

    if len(A) == 2:
        _1, _2 = A
        return [[_1, _2], [_2, _1]]

    perms = permutations(A[1:])

    result = []
    for i in range(len(A)):
        for p in perms:
            result.append((p[0:i]+[A[0]]+p[i:]))


    return result


def test(A: List[int], expected: List[List[int]]):
    actual = permutations(A)

    assert actual == expected, f"{A}, expected {expected}, got {actual}"


if __name__ == '__main__':
    test([1], [[1]])
    test([1, 2], [[1, 2], [2, 1]])
    test([1, 2, 3], [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [3, 1, 2],
        [2, 3, 1],
        [3, 2, 1],
    ])
    sys.exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
