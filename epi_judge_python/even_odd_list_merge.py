import sys
from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    odd_list_head = ListNode(None)
    odd_list_browser = odd_list_head

    even_list_head = ListNode(None)
    even_list_browser = even_list_head

    is_even = True
    list_browser = L

    while list_browser:
        if is_even:
            even_list_browser.next = list_browser
            even_list_browser = even_list_browser.next
        else:
            odd_list_browser.next = list_browser
            odd_list_browser = odd_list_browser.next

        list_browser = list_browser.next
        is_even = not is_even

    even_list_browser.next = odd_list_head.next
    odd_list_browser.next = None

    return even_list_head.next


if __name__ == '__main__':
    sys.exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
