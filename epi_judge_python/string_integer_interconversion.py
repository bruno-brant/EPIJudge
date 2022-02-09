import enum
from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if x == 0:
        return '0'

    is_negative = x < 0

    if is_negative:
        x = abs(x)

    as_str = ''

    while True:
        digit = x % 10
        as_str = str(digit) + as_str
        x -= digit
        x /= 10
        x = int(x)

        if x == 0:
            break

    if is_negative:
        as_str = '-' + as_str

    return as_str


def string_to_int(s: str) -> int:
    result = 0
    is_negative = s[0] == '-'

    if is_negative or s[0] == '+':
        s = s[1:]

    for _, value in enumerate(s):
        result = (10 * result) + int(value)

    if is_negative:
        result = -result

    return result


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


def test(as_int: int, as_str: str):
    actual_str = int_to_string(as_int)
    assert actual_str == as_str, f"int_to_string -> expected {as_str}, got {actual_str}"
    actual_int = string_to_int(as_str)
    assert actual_int == as_int, f"string_to_int -> expected {as_int}, got {actual_int}"


if __name__ == '__main__':
    test(0, "0")
    test(1, "1")
    test(12, "12")
    test(-1, "-1")

    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
