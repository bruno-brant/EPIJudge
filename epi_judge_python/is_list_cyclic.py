import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def has_cycle(head: ListNode) -> Optional[ListNode]:
    seen = set()

    while head.next:
        if id(head) in seen:
            return head

        seen.add(id(head))
        head = head.next

    return None


def has_cycle_optimal(head: ListNode) -> Optional[ListNode]:
    """
    Optimal implementation of the has cycle problem (the book)
    [I knew how to implement the two pointers approach, but not how to get
    the start of the cycle - I was looking for something better]
    """

    if head is None:
        return None

    slow = head
    fast = head.next

    while fast is not None and id(slow) != id(fast):
        slow = slow.next

        if fast.next is None:
            return None

        fast = fast.next.next

    if fast is None:
        return None

    # Calculate the Cycle length C

    C = 1
    while id(fast.next) != id(slow):
        C += 1
        fast = fast.next

    def advance(node: ListNode, n: int):
        while n > 0:
            node = node.next
            n -= 1
        return node

    slow = head
    fast = advance(head, C)

    while id(slow) != id(fast):
        slow = slow.next
        fast = fast.next

    return slow


@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError('Can\'t cycle empty list')
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError('Can\'t find a cycle start')
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle_optimal, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure('Found a non-existing cycle')
    else:
        if result is None:
            raise TestFailure('Existing cycle was not found')
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    'Returned node does not belong to the cycle or is not the closest node to the head'
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            'Returned node does not belong to the cycle or is not the closest node to the head'
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_cyclic.py',
                                       'is_list_cyclic.tsv',
                                       has_cycle_wrapper))
