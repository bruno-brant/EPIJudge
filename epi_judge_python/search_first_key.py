from threading import Timer
from typing import List
from math import floor
from test_framework import generic_test
from test_framework.timed_executor import TimedExecutor


def search_first_of_k(A: List[int], k: int) -> int:
    l = 0 
    r = len(A) - 1
    result = -1

    while l <= r:
        m = floor(l + ((r - l) / 2)) # avoid overflow

        if k < A[m]:
            r = m - 1
        elif k > A[m]:
            l = m + 1
        else:
            result = m
            r = m - 1

    return result


def test(array, target, expected):
    executor = TimedExecutor(60)
    actual = executor.run(lambda: search_first_of_k(array, target))
    assert actual == expected, f"Expected {expected}, got {actual}"

    print(f"Duration {floor(executor.get_timer().get_microseconds() / 1000)} ms")

if __name__ == '__main__':
    very_long_sample = [10 for i in range(10_000_000)]
    print("Begin long test")
    test(very_long_sample, 10 ,0)
    print("Finish long test")

    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
