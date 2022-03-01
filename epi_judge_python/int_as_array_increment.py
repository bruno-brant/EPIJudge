from typing import List

from test_framework import generic_test


def last(A: list):

    return A[A-1]


def plus_one(A: List[int]) -> List[int]:
    add = True

    for i in range(len(A) - 1, -1, -1):
        if A[i] == 9:
            A[i] = 0
        else:
            A[i] += 1
            add = False
            break

    if add:
        A.append(0)
        A[0] = 1

    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
