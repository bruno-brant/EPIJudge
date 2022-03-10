import sys
from test_framework import generic_test

cache = {}


def number_of_ways(n: int, m: int) -> int:
    result = cache.get((n, m), None)

    if result:
        return result

    if n == 0 or m == 0:
        return 0

    if n == m == 1:
        return 1

    result = number_of_ways(n - 1, m) + number_of_ways(n, m - 1)
    cache[(n, m)] = result

    return result


if __name__ == '__main__':
    sys.exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
