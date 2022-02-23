from typing import Optional

from bst_node import BstNode, TreeSpec
from test_framework import generic_test


def find_first_greater_than_k(tree: BstNode, k: int, first_greater: BstNode = None) -> Optional[BstNode]:
    if tree is None:
        return first_greater

    if tree.data > k and (first_greater is None or first_greater.data > tree.data):
        first_greater = tree
        
        return find_first_greater_than_k(tree.left, k, first_greater)
    
    # tree.data <= k
    return find_first_greater_than_k(tree.right, k, first_greater)


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


def test(arr: TreeSpec, k: int, expected: int):
    tree = BstNode.from_array(arr)
    actual = find_first_greater_than_k(tree, k)

    if actual is None and expected is None:
        return

    actual = actual.data

    assert expected == actual, f"Tree: {arr}, expected {expected}, got {actual}"


if __name__ == '__main__':
    # test([2, [1], [7]], 5, 7)

    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
