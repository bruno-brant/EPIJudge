import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def number_of_nodes(head: ListNode):
    n = 0

    while head is not None:
        n += 1
        head = head.next

    return n


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    if l0 is None or l1 is None:
        return None

    len_l0 = number_of_nodes(l0)
    len_l1 = number_of_nodes(l1)

    larger, smaller = (l0, l1) if len_l0 > len_l1 else (l1, l0)

    diff = abs(len_l0 - len_l1)

    for _ in range(diff):
        larger = larger.next

    while larger.next is not None and smaller.next is not None:
        if id(larger) == id(smaller):
            return larger

        larger = larger.next
        smaller = smaller.next

    return None


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
