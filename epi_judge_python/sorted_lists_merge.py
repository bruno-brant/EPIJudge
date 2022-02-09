from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    if L1 == None:
        return L2

    if L2 == None:
        return L1

    head = L1

    # Reorder so that L1 is always the head
    if L2.data < L1.data:
        head = L2
        L2 = L1
        L1 = head

    while L1 != None and L2 != None:
        if L1.next != None and L1.next.data < L2.data:
            L1 = L1.next
        else:
            old_L1_next = L1.next
            old_L2_next = L2.next

            L1.next = L2
            L2.next = old_L1_next
            L2 = old_L2_next
            L1 = L1.next

    return head


def test(L1: list[int], L2: list[int], expected: list[int]):
    L1_ll = ListNode.from_array(L1)
    L2_ll = ListNode.from_array(L2)
    expected_ll = ListNode.from_array(expected)

    actual = merge_two_sorted_lists(L1_ll, L2_ll)
    assert actual == expected_ll, f"Expected {expected_ll}, got {actual}"


if __name__ == '__main__':
    test([], [], [])
    test([1], [], [1])
    test([], [1], [1])
    test([-14, -13, -9, -6, -5, -2, -1, 1, 4, 7, 8, 10, 12, 13],
         [-25, -23, -18, -18, -14, -8, -8, -6, -3, -2, -1, 2, 5,
             8, 8, 8, 12, 12, 12, 14, 14, 20, 20, 22, 25, 26],
         [-25, -23, -18, -18, -14, -14, -13, -9, -8, -8, -6, -6, -5,  -3, -2, -2, -1, -1,
             1, 2, 4, 5, 7, 8, 8, 8, 8, 10, 12, 12, 12, 12, 13, 14, 14, 20, 20, 22, 25, 26]
         )

    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
