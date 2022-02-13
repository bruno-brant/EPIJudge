import sys
from test_framework import generic_test


def power(x: float, y: int) -> float:
    if y == 0:
        return 1

    if y == 1:
        return x

    if y == 2:
        return x * x

    if y < 0:
        return 1 / power(x, -y)

    if y % 2 == 0:
        p = power(x, y / 2)
        return  p * p

    return power(x, y - 1) * x


def test(x, y):
    expected = pow(x, y)
    actual = power(x, y)

    assert float_eq(
        expected, actual), f"{x}^{y}: expected {expected}, got {actual}"


def float_eq(a: float, b: float) -> bool:
    diff = abs(a) - abs(b)
    return diff < sys.float_info.epsilon


if __name__ == '__main__':
    test(0, 1)
    test(1, 1)
    test(2, 2)
    test(2, 3)
    test(2, 10)
    test(3, 2)
    test(3, 4)

    test(1.5, 2)
    test(0.5, 2)

    test(0.001, 2)
    test(0.001, 100)

    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
