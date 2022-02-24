from typing import List

from test_framework import generic_test


Board = List[List[int]]


def n_queens(n: int) -> List[List[int]]:
    placement = [None for _ in range(n)]
    results = []

    n_queens_impl(n, placement, 0, results)

    return results


def is_valid(placement: List[int], row_idx: int):
    for i in range(row_idx):
        if placement[i] == placement[row_idx]:
            return False
        if abs(row_idx - i) == abs(placement[row_idx] - placement[i]):
            return False
    return True


def n_queens_impl(n: int, placement: List[int], row_idx, results: List[List[int]]):
    if row_idx == n:
        results.append(placement.copy())
        return

    for c in range(n):
        placement[row_idx] = c

        if is_valid(placement, row_idx):
            n_queens_impl(n, placement, row_idx + 1, results)


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
