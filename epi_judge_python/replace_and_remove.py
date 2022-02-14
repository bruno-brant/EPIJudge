from asyncore import write
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Replace a with d, d and delete b
def replace_and_remove(size: int, s: List[str]) -> int:
    # Count 'a' and remove 'b'
    count_a = 0
    count_b = 0
    read_idx = 0
    write_idx = 0

    while read_idx < size:
        if s[read_idx] == 'a':
            count_a += 1
        elif s[read_idx] == 'b':
            count_b += 1
            write_idx -= 1

        read_idx += 1
        write_idx += 1

        s[write_idx] = s[read_idx]

    read_idx = size - count_b - 1
    size = size - count_b + count_a
    write_idx = size - 1

    while read_idx >= 0 and write_idx >= 0:
        c = s[read_idx]

        if c == 'a':
            s[write_idx] = 'd'
            s[write_idx - 1] = 'd'
            write_idx -= 1
        else:
            s[write_idx] = s[read_idx]

        read_idx -= 1
        write_idx -= 1

    return size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


def test(_str: str, size: int, expected: str):
    actual = replace_and_remove(size, _str)
    assert len(
        expected) == actual, f'Expected a string of length {len(expected)}, got {actual}'
    assert _str[:actual] == expected, f'Expected {expected}, got {actual}'


if __name__ == '__main__':
    # test(['c'], 1, ['c'])
    # test(['a', ''], 1, ['d', 'd'])
    # test(['a', 'b'], 1, ['d', 'd'])
    # test(['a', 'b'], 1, ['d', 'd'])
    # test(['b', 'd', 'c', 'a', 'b', ''], 5, ['d', 'c', 'd', 'd'])

    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
