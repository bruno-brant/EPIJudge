from typing import List

from test_framework import generic_test

[448, 381, 227, 992, -529, 21]


def find_maximum_subarray(A: List[int]) -> int:
    max_ = 0
    subarray = 0
    for item in A:
        subarray = subarray + item if subarray + item > item else item
        max_ = max(max_, subarray)

    return max_


if __name__ == '__main__':
    input = [448, 381, 227, 992, -529, 21, 508, 468, -910, -614, 503, -127, -710, -372, 185, 495, -920, -886, 792, -108, -648, -662, -922, 242, -892, 954, -479, -575, 939, 269, 5, 733,
             700, 907, 55, -838, -666, -287, -196, -674, 350, 774, 647, 384, -35, -861, -820, -795, 516, -57, -646, -325, -159, 856, -636, 168, 675, 852, -105, -731, 780, 592, -20, 843, 476, 3]

    assert find_maximum_subarray(input) == 3753, "Failed"

    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
