import sys
from typing import Iterator, List

from test_framework import generic_test
from utilities import MaxHeap, MinHeap


def online_median(sequence: Iterator[int]) -> List[float]:
    upper = MinHeap()
    lower = MaxHeap()
    median = 0
    result = []

    for i in sequence:
        if i > median:
            upper.push(i)
        else:
            lower.push(i)

        # balance
        diff = len(upper) - len(lower)

        if diff > 1:
            lower.push(upper.pop())
        elif diff < -1:
            upper.push(lower.pop())

        if len(lower) == len(upper):
            median = (upper.peek() + lower.peek()) / 2
        elif len(lower) < len(upper):
            median = upper.peek()
        elif len(upper) < len(lower):
            median = lower.peek()

        result.append(median)

    return result


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    sys.exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
