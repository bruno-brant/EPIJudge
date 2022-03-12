import sys
from typing import Iterator

from test_framework import generic_test


class Majority:
    def __init__(self, value, count) -> None:
        self.value = value
        self.count = count

    def __repr__(self) -> str:
        return f"{self.value} ({self.count})"

def majority_search(stream: Iterator[str]) -> str:

    majority = None

    for i in stream:
        if majority is None:
            majority = Majority(i, 1)

        else:
            if i == majority.value:
                majority.count += 1
            else:
                if majority.count == 1:
                    majority = None
                else:
                    majority.count -= 1

    return majority.value


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


def test(values, expected):
    actual = majority_search(values)

    assert actual == expected, f"Expected {expected}, got {actual}"


if __name__ == '__main__':
    test(["9", "49", "20", "34", "36", "36", "35", "9", "38", "9", "9", "7", "9", "9", "50", "9", "9", "9", "53", "9", "9", "18", "9", "6", "9", "20", "49", "47", "12", "9", "14", "8", "39", "9", "9", "9", "9", "9", "9", "9", "9", "9", "49", "9", "9", "9", "37", "9", "26", "27", "9", "35", "41", "21", "9", "9", "9", "9", "7", "9",
         "9", "12", "9", "9", "9", "9", "44", "54", "58", "27", "9", "30", "9", "9", "19", "9", "13", "5", "44", "46", "50", "9", "9", "41", "6", "9", "9", "33", "9", "9", "1", "9", "9", "9", "9", "1", "32", "9", "28", "9", "55", "36", "40", "43", "33", "43", "9", "50", "21", "9", "9", "33", "35", "9", "9", "9", "34", "31"], "9")
    sys.exit(
        generic_test.generic_test_main('majority_element.py',
                                       'majority_element.tsv',
                                       majority_search_wrapper))
