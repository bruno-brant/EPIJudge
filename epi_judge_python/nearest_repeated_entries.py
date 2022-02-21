from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    min_distance = len(paragraph) + 1

    word_position = {}

    for i, word in enumerate(paragraph):
        if word in word_position:
            last_position = word_position[word]

            distance = i - last_position

            min_distance = min(min_distance, distance)

        word_position[word] = i

    return -1 if min_distance == len(paragraph) + 1 else min_distance


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
