import sys
from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


class InorderTraversal:
    def __init__(self) -> None:
        self._last_node: BinaryTreeNode = None
        self._browser: BinaryTreeNode = None

    def inorder_traversal(self, tree: BinaryTreeNode) -> List[int]:
        self._last_node: BinaryTreeNode = None
        self._browser: BinaryTreeNode = tree

        while self._browser:
            if self._last_was_left():
                yield self._browser.data
                if self._browser.right:
                    self._go_right()
                else:
                    self._go_up()
            elif self._last_was_right():
                self._go_up()
            elif self._browser.left:
                self._go_left()
            else:
                yield self._browser.data

                if self._browser.right:
                    self._go_right()
                else:
                    self._go_up()

    def _last_was_left(self):
        return self._last_node is not None and self._last_node == self._browser.left

    def _last_was_right(self):
        return self._last_node is not None and self._last_node == self._browser.right

    def _go_left(self):
        self._last_node = self._browser
        self._browser = self._browser.left

    def _go_right(self):
        self._last_node = self._browser
        self._browser = self._browser.right

    def _go_up(self):
        self._last_node = self._browser
        self._browser = self._browser.parent


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    trav = InorderTraversal()
    return list(trav.inorder_traversal(tree))


if __name__ == '__main__':
    sys.exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
