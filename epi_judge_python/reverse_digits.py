import sys

from test_framework import generic_test


def reverse(x: int) -> int:
    if x < 0:
        is_negative = -1
        x = abs(x)
    else:
        is_negative = 1

    result = 0

    while x != 0:
        result = (result * 10) + (x % 10)
        x /= 10
        x = int(x)

    return is_negative * result


assert reverse(1) == 1
assert reverse(10) == 1
assert reverse(100) == 1
assert reverse(1000) == 1
assert reverse(12) == 21

if __name__ == '__main__':
    sys.exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
