from typing import List

from test_framework import generic_test

from matrix import make_matrix


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    lines = len(individual_play_scores)
    columns = final_score + 1

    A = make_matrix(lines, columns)

    for i, play_score in enumerate(individual_play_scores):
        for j in range(len(A[i])):
            if j == 0:
                A[i][j] = 1
            elif i == 0 and j % play_score == 0:
                A[i][j] = 1
            else:
                A[i][j] = A[i-1][j]

                if j >= play_score:
                    A[i][j] += A[i][j-play_score]

    return A[-1][-1]


def test(score, individual_scores, expected):
    actual = num_combinations_for_final_score(score, individual_scores)

    msg = f"For {score} with {individual_scores} expected {expected}, got {actual}"

    assert actual == expected, msg


if __name__ == '__main__':
    test(1, [1], 1)
    test(2, [1, 2], 2)
    test(3, [1, 3], 2)
    test(3, [1, 2], 2)
    # 1 1 b
    # 1 2
    # 2 1
    test(4, [2], 1)
    test(4, [1, 3], 2)
    test(4, [1, 2, 3], 4)
    # 1 1 1 1

    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
