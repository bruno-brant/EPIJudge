import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reverse_word(s: List[str], start: int, end: int):
    while start < end:
        s[start], s[end] = s[end], s[start]
        
        start += 1
        end -= 1

# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].


def reverse_words(s: List[str]):
    i = 0
    j = len(s) - 1

    # reverse the whole array
    reverse_word(s, i, j)

    # reverse each word
    start = 0
    for i, c in enumerate(s):
        if c == ' ':
            reverse_word(s, start, i - 1)
            start = i + 1

        if i == len(s) - 1:
            reverse_word(s, start, i)
            start = i + 1

    return s


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
