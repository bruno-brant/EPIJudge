from math import floor
from test_framework import generic_test


def int_square_root(k: int) -> int:
    if k <= 1:
        return k

    l = 0
    r = k
    m = k

    while l < r - 1:
        m = l + ((r - l) // 2)
        m2 = m * m

        if m2 == k:
            return floor(m)
        elif m2 < k:
            l = m
        else:  # m2 > k
            r = m

    return l + ((r - l) // 2)

if __name__ == '__main__':
    assert int_square_root(3) == 1

    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', int_square_root))
