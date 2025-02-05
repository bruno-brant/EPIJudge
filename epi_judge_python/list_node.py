from typing import List


class ListNode:
    def __init__(self, data=0, next_: 'ListNode' = None):
        self.data = data
        self.next = next_

    def __eq__(self, other):
        a, b = self, other
        while a and b:
            if a.data != b.data:
                return False
            a, b = a.next, b.next
        return a is None and b is None

    def __repr__(self):
        node = self
        visited = set()
        first = True

        result = ''

        while node:
            if first:
                first = False
            else:
                result += ' -> '

            if id(node) in visited:
                if node.next is not node:
                    result += str(node.data)
                    result += ' -> ... -> '

                result += str(node.data)
                result += ' -> ...'
                break
            else:
                result += str(node.data)
                visited.add(id(node))
            node = node.next

        return result

    def __str__(self):
        return self.__repr__()

    # def __len__(self):
    #     browser = self
    #     l = 0
    #     while browser is not None:
    #         l += 1
    #         browser = browser.next

        return l

    @staticmethod
    def from_array(arr: List[int]):
        if len(arr) == 0:
            return None

        head = ListNode(arr[0])

        browser = head
        for i in range(1, len(arr)):
            browser.next = ListNode(arr[i])
            browser = browser.next

        return head


def list_size(node):
    result = 0
    visited = set()

    while node is not None and id(node) not in visited:
        result += 1
        visited.add(id(node))
        node = node.next

    return result
