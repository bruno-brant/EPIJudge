from typing import Optional, Tuple
from test_framework.binary_tree_utils import (binary_tree_to_string,
                                              equal_binary_trees)


TreeSpec = Tuple[int, Optional['TreeSpec'], Optional['TreeSpec']]


class BstNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

    def __eq__(self, other):
        return equal_binary_trees(self, other)

    def __repr__(self):
        return str(binary_tree_to_string(self))

    def __str__(self):
        return self.__repr__()

    @staticmethod
    def from_array(arr: TreeSpec) -> 'BstNode':
        if not arr:
            return None

        left = BstNode.from_array(arr[1]) if len(arr) > 1 else None
        right = BstNode.from_array(arr[2]) if len(arr) > 2 else None

        return BstNode(arr[0], left, right)
