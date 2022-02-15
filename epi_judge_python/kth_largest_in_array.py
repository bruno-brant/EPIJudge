from random import randint
from typing import List

from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    l = 0
    r = len(A) - 1
    
    while l < r:
        pivot = randint(l, r)
        pivot = partition(A, l, r, pivot)

        nth_largest = r - pivot + 1
        
        if nth_largest == k:
            return A[pivot]
        
        if nth_largest < k:
            k -= nth_largest
            r = pivot - 1
        else: # r - pivot > k
            l = pivot
    
    return A[l]

def partition(A: List[int], l: int, r: int, pivot: int) -> int:
    # swap pivot with the start of the array
    A[l], A[pivot] = A[pivot], A[l]
    pivot = l
    l += 1

    while l < r:
        if A[l] < A[pivot]:
            l += 1
        elif A[l] > A[pivot]:
            A[r], A[l]  = A[l], A[r]
            r -= 1

    if A[l] > A[pivot]:
        A[l - 1], A[pivot] = A[pivot], A[l - 1]
        pivot = l - 1
    else:
        A[l], A[pivot] = A[pivot], A[l]
        pivot = l

    return pivot

def test_partition(A: List[int], l: int, r: int, pivot: int, expected: List[int]):
    pivot = partition(A, l, r, pivot)
    
    pivot_value = A[pivot]
    for i in range(l, pivot):
        if A[i] > pivot_value:
            raise f"Wrong value at {i}, got {A[i]} which is greater than {pivot_value}."

    for i in range(pivot + 1, r + 1):
        if A[i] < pivot_value:
            raise f"Wrong value at {i}, got {A[i]} which is lesser than {pivot_value}."

    assert pivot == expected, f"Expected {expected}, got {pivot}"


def test(k: int, A: List[int], expected: int):
    actual = find_kth_largest(k, A)

    assert actual == expected, f"Expected {expected}, got {actual}"


if __name__ == '__main__':
    test_partition([5, 4, 3, 2, 1], 0, 4, 2, 2)
    test_partition([5, 4, 3, 2, 1], 2, 4, 3, 3)

    test(1, [3, 1, -1, 2], 3)
    test(2, [3, 1, -1, 2], 2)
    test(3, [3, 1, -1, 2], 1)
    test(4, [3, 1, -1, 2], -1)
    test(1, [-1], -1)

    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
