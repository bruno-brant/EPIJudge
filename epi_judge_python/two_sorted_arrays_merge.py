from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:

    if n == 0:
        return

    write_index = m + n
    Aidx = m - 1
    Bidx = n - 1

    while write_index >= 0:
        write_index -= 1
        
        if Aidx >= 0 and A[Aidx] >= B[Bidx]:
            A[write_index] = A[Aidx]
            Aidx -= 1
        elif Bidx >= 0:
            A[write_index] = B[Bidx]
            Bidx -= 1

def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
