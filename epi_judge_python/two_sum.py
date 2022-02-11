from typing import List

from test_framework import generic_test


def has_two_sum(A: List[int], t: int) -> bool:
    l, r = 0, len(A) - 1

    while l <= r:
        if A[l] + A[r] == t:
            return True
        if A[l] + A[r] < t:
            l += 1
        else: # A[l] + A[r] > t:
            r -= 1

    return False

# 6
#
# 1 2 4 5 8
# l       r
#       r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sum.py', 'two_sum.tsv',
                                       has_two_sum))
