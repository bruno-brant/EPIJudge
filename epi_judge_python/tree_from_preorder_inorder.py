import sys
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


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
    in_left = inorder[0:pivot]
    in_right = inorder[pivot+1:]
    pre_left = list(filter(lambda p: p in in_left, preorder))
    pre_right = list(filter(lambda p: p in in_right, preorder))

    return BinaryTreeNode(head,
                          binary_tree_from_preorder_inorder(pre_left, in_left),
                          binary_tree_from_preorder_inorder(pre_right, in_right))


if __name__ == '__main__':
    sys.exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
