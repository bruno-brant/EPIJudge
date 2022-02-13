from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    def get(i, j):
        return square_matrix[i][j]

    min, max = 0, len(square_matrix) - 1

    if max < 0:
        return []

    i, j = 0, 0
    L = [get(i, j)]
    while max >= min:
        # left
        while j < max:
            j += 1
            L.append(get(i, j))
        # down
        while i < max:
            i += 1
            L.append(get(i, j))
        # right
        while j > min:
            j -= 1
            L.append(get(i, j))

        min += 1
        max -= 1

        # up
        while i > min:
            i -= 1
            L.append(get(i, j))

    return L


def test(square_matrix: List[List[int]], expected: List[int]):
    actual = matrix_in_spiral_order(square_matrix)
    assert expected == actual, f"Expected {expected}, got {actual}"


if __name__ == '__main__':
    # test([], [])
    test([[5]], [5])
    test([[4, 5], [7, 6]], [4, 5, 6, 7])

    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
