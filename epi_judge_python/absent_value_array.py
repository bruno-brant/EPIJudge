from itertools import tee
from typing import Iterator

from test_framework import generic_test
from test_framework.test_failure import TestFailure


def find_missing_element(stream: Iterator[int]) -> int:
    # From the book, we are going to use an array with 2^16 positions.

    stream, stream2 = tee(stream, 2)
    k64 = 1 << 16
    buckets = [0]*(k64)

    for ip in stream:
        high = ip >> 16
        buckets[high] += 1

    high = None
    for high, count in enumerate(buckets):
        if count < k64:
            break

    if high is None:
        return -1

    bitset = [False] * k64
    for ip in stream2:
        low = ip & ((k64) - 1)
        bitset[low] = True

    for low, in_file in enumerate(bitset):
        if not in_file:
            return low  | (high << 16)

    return 0


def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise TestFailure('{} appears in stream'.format(res))
    except ValueError:
        raise TestFailure('Unexpected no missing element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('absent_value_array.py',
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
