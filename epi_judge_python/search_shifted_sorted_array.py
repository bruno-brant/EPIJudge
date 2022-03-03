from math import ceil
from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    """
    We kinda do a binary search. 

    What we can notice is that, whenever we bipartition the array, if the range 
    seems to be decreasing, i.e., start > end of the range, then we *know* that the 
    smallest number must be in there.

    So we keep partitioning until we find a number A[n] which is smaller than A[n - 1]. 

    Special case for when the array is actually sorted and non-shifted - in this case,
    the array will seem to be always increasing, therefore, it's smallest number is it's start

    """

    l, r = 0, len(A) - 1

    if A[l] < A[r]:
        return l

    while r - l > 1:

        m = ceil((l + r) / 2)

        if A[l] > A[m]:
            r = m
        else:
            l = m

    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
