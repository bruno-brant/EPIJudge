import functools
import sys
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class Event:
    def __init__(self, start: int = None, finish: int = None):
        self.start = start
        self.finish = finish

    def __repr__(self) -> str:
        return f'({self.start}, {self.finish})'

    def __str__(self):
        return self.__repr__()


class Endpoint:
    def __init__(self, value: int, is_start: bool) -> None:
        self.value = value
        self.is_start = is_start

    def __eq__(self, __o: object) -> bool:
        if __o == None:
            return False

        return self.value == __o.value and self.is_start == __o.is_start

    def __lt__(self, __o: 'Endpoint'):
        if self.value < __o.value:
            return True

        if self.value == __o.value:
            return (self.is_start and not __o.is_start)

        return False


def find_max_simultaneous_events(A: List[Event]) -> int:
    endpoints: List[Endpoint] = []

    for i in A:
        endpoints.append(Endpoint(i.start, True))
        endpoints.append(Endpoint(i.finish, False))

    endpoints = sorted(endpoints)

    max_height = height = 0
    for e in endpoints:
        if e.is_start:
            height += 1
        else:
            height -= 1
        max_height = max(max_height, height)

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
