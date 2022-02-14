import sys
from typing import List, Optional

from list_node import ListNode
from test_framework import generic_test

def reverse_sublist_reference_impl(head: ListNode, start: int, finish: int) -> Optional[ListNode]:
    dummy_head = ListNode(None, head)
    sublist_head = dummy_head
    k = 1
    while k < start:
        sublist_head = sublist_head.next
        k += 1

    sublist_iter = sublist_head.next
    while k < finish:
        k += 1
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp

    return dummy_head.next

def reverse_sublist(head: ListNode, start: int, finish: int) -> Optional[ListNode]:
    if start == finish:
        return head

    start -= 1
    finish -= 1

    # Find the first node
    browser = head
    previous = None
    
    for _ in range(start):
        previous = browser
        browser = browser.next
    
    start_node_parent = previous
    start_node = browser

    # Invert the sublist
    previous = browser
    browser = browser.next
    start_node.next = None

    for _ in range(finish - start):
        current = browser
        browser = browser.next
        current.next = previous
        previous = current

    end_node = previous
    follow_node = browser
    
    start_node.next = follow_node

    if start_node_parent is None:
        return previous

    start_node_parent.next = end_node

    return head

def test(A: List[int], start: int, end: int, expected: List[int]):
    L = ListNode.from_array(A)
    actual = reverse_sublist(L, start, end)
    expected = ListNode.from_array(expected)
    assert actual == expected, f"Expected {expected}, got {actual}"


if __name__ == '__main__':
    test([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5])
    test([1, 2, 3], 2, 2, [1, 2, 3])
    test([1], 0, 0, [1])
    test([1, 2, 3], 1, 3, [3, 2, 1])

    sys.exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
