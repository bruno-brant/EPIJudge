import functools
import sys
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from utilities import Heap

# Event is a tuple (start_time, end_time)


class Event:
    def __init__(self, start: int = None, finish: int = None):
        self.start = start
        self.finish = finish

    def __repr__(self) -> str:
        return f'({self.start}, {self.finish})'

    def __str__(self):
        return self.__repr__()


def find_max_simultaneous_events(A: List[Event]) -> int:
    overlapping = Heap[Event](lambda a, b: a.finish < b.finish)

    A = sorted(A, key=lambda _: _.start)

    max_height = 0

    for a in A:
        while overlapping and overlapping.peek().finish < a.start:
            overlapping()

        overlapping += a
        max_height = max(max_height, len(overlapping))

    return max_height


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))
#            00000000001111111111
#            01234567890123456789
# [1, 5]      -----
# [2, 7]       ------
# [4, 5]         --

# [6, 10]          -----
# [8, 9],            --
# [9, 10]             --
# [9, 17]             ---------

# [11, 13]              ---
# [12, 15]               ----
# [14, 15]                 --
#


if __name__ == '__main__':
    sys.exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
