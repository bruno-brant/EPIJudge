import sys

from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from utilities import Slice


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    """
    The first item in the preorder identifies the head.
    Everything to the left of the head in the inorder is to the left of the head. 
    Everything to the right of the head in the inorder is to the right of the head.

    So we check who is the head in the inorder, find it in the preorder partitioning it, 
    filter the preorder with what is in the inorder, and call recursively
    """

    if not preorder:
        return None

    head = preorder[0]
    pivot = inorder.index(head)

    in_left = Slice(inorder, 0, pivot)
    pre_left = Slice(preorder, 1, 1 + len(in_left))

    in_right = Slice(inorder, pivot + 1)
    pre_right = Slice(preorder, 1 + pivot, 1 + pivot + len(in_right))

    return BinaryTreeNode(head,
                          binary_tree_from_preorder_inorder(pre_left, in_left),
                          binary_tree_from_preorder_inorder(pre_right, in_right))


if __name__ == '__main__':
    sys.exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
