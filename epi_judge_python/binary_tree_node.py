from test_framework.binary_tree_utils import (binary_tree_to_string,
                                              equal_binary_trees)


class BinaryTreeNode:
    def __init__(self, data: int = None, left: 'BinaryTreeNode' = None, right: 'BinaryTreeNode' = None):
        self.data = data
        self.left = left
        self.right = right

    def __eq__(self, other):
        return equal_binary_trees(self, other)

    def __repr__(self):
        return str(binary_tree_to_string(self))

    def __str__(self):
        return self.__repr__()

    @staticmethod
    def from_array(arr: list):
        if arr == None:
            return None

        l = len(arr)

        value = arr[0] if l >= 1 else None
        left = BinaryTreeNode.from_array(arr[1]) if l >= 2 else None
        right = BinaryTreeNode.from_array(arr[2]) if l >= 3 else None

        return BinaryTreeNode(value, left, right)
