from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    result = []

    find_k_largest_in_bst_impl(tree, k, result)

    return result


def find_k_largest_in_bst_impl(tree: BstNode, k: int, result: List[int]) -> List[int]:
    if tree.right:
        find_k_largest_in_bst_impl(tree.right, k, result)

    if len(result) < k:
        result.append(tree.data)

    if tree.left:
        find_k_largest_in_bst_impl(tree.left, k, result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
