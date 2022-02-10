from typing import List
from math import floor
from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    l = 0 
    r = len(A) - 1

    while l <= r:
        m = floor(l + ((r - l) / 2)) # avoid overflow

        if k < A[m]:
            r = m - 1
        elif k > A[m]:
            l = m + 1
        else:
            while m > 0 and A[m-1] == k:
                m -= 1
            return m

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
