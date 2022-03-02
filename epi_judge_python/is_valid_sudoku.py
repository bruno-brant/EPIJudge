from enum import Enum
from typing import List

from test_framework import generic_test


class Validity(Enum):
    Valid = 1,
    Invalid = 0


class DigitsPool:
    def __init__(self) -> None:
        self._is_digit_used = [0] * 10

    def check_digit(self, digit: int) -> Validity:
        self._is_digit_used[digit] += 1

        if self._is_digit_used[digit] > 1:
            return Validity.Invalid

        return Validity.Valid

    def __repr__(self) -> str:
        return repr(self._is_digit_used)

    def __str__(self) -> str:
        return str(self._is_digit_used)


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    rows = [DigitsPool() for _ in range(9)]
    columns = [DigitsPool() for _ in range(9)]
    mini_matrices = [[DigitsPool() for _ in range(3)] for _ in range(3)]

    for row in range(9):
        for column in range(9):
            digit = partial_assignment[row][column]

            if digit == 0:
                continue

            if rows[row].check_digit(digit) == Validity.Invalid:
                return False

            if columns[column].check_digit(digit) == Validity.Invalid:
                return False

            if mini_matrices[row // 3][column // 3].check_digit(digit) == Validity.Invalid:
                return False

    return True


if __name__ == '__main__':
    m = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 1],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 4, 0, 9],
        [0, 0, 0, 5, 0, 4, 0, 0, 0]
    ]

    #test(m, True)

    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
