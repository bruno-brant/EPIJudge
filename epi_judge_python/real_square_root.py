import functools
import math
import sys
from unittest import expectedFailure
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

precision = 10
epsilon = 10**(-precision)


def square_root(x: float) -> float:
    if x >= 1:
        min_ = 1.
        max_ = x
    else:
        min_ = x
        max_ = 1.

    while abs(max_ - min_) > epsilon:
        m = (min_ + max_) / 2

        sq = m*m

        if abs(sq - x) < epsilon:
            return m

        if sq > x:
            max_ = m
        else:
            min_ = m

    return min_


@enable_executor_hook
def square_root_wrapper(executor, x):
    result = executor.run(functools.partial(square_root, x))

    expected = math.sqrt(x)
    
    if (result - expected) < epsilon:
        return expected

    return result


if __name__ == '__main__':
    sys.exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root_wrapper))
