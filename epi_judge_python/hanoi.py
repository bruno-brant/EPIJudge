import functools
from tkinter import Y
from typing import Iterator, List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3


def compute_tower_hanoi(num_rings: int, from_peg=0, to_peg=2) -> List[List[int]]:
    return list(compute_tower_hanoi_impl(num_rings, from_peg, to_peg))


def compute_tower_hanoi_impl(num_rings: int, from_peg=0, to_peg=2) -> Iterator[List[int]]:
    auxiliar_peg = [0, 1, 2]
    auxiliar_peg.remove(from_peg)
    auxiliar_peg.remove(to_peg)
    auxiliar_peg = auxiliar_peg[0]

    if num_rings == 1:
        yield [from_peg, to_peg]

    elif num_rings == 2:
        yield [from_peg, auxiliar_peg]
        yield [from_peg, to_peg]
        yield [auxiliar_peg, to_peg]

    else:
        for move in compute_tower_hanoi(num_rings-1, from_peg, auxiliar_peg):
            yield move

        yield [from_peg, to_peg]

        for move in compute_tower_hanoi(num_rings-1, auxiliar_peg, to_peg):
            yield move


@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))
            ] + [[] for _ in range(1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure('Illegal move from {} to {}'.format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure('Pegs doesn\'t place in the right configuration')

# def test(num_rings):
#     pegs = [num_rings, 0, 0]

#     for move in compute_tower_hanoi(num_rings):
        

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('hanoi.py', 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
