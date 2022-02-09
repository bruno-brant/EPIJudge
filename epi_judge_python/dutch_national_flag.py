import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def swap(A: List[int], idx_a: int, idx_b: int):
    b = A[idx_b]
    A[idx_b] = A[idx_a]
    A[idx_a] = b


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    less_idx = 0
    greater_idx = len(A) 
    pivot = A[pivot_index]

    i = 0

    while i < greater_idx:
        if A[i] < pivot:
            swap(A, less_idx, i)
            less_idx += 1
            i += 1
        elif A[i] > pivot:
            greater_idx -= 1
            swap(A, greater_idx, i)
        else:
            i += 1


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A: List[int], pivot_idx: int):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    # A = [1, 0, 2, 0, 2, 1, 2, 1, 2, 0, 0, 0, 1, 0, 2, 1, 0, 2, 0, 1, 0, 2, 1, 0, 2, 1, 2, 0, 2, 1, 1, 2, 2, 0, 1, 1, 0, 1, 1, 1, 2, 1, 0, 1, 2, 1, 2, 1, 2, 2, 2, 0, 1, 0, 1, 1, 2, 1, 1, 2, 2, 1, 1, 1, 0, 2, 0, 1, 2, 1, 1, 1, 0, 2, 0, 1, 2, 1, 1, 2, 1, 2, 2, 1, 0, 1, 2, 2, 1, 2, 2, 1, 1, 2, 0, 1, 0, 1, 2, 0, 2, 1, 2, 1, 1, 1, 2, 2, 2, 0, 0, 0, 1, 2, 0, 0, 0, 0]
    # dutch_flag_partition(0,  A)
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
