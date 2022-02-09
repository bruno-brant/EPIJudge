from typing import Tuple
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def is_balanced_binary_tree_impl(tree: BinaryTreeNode) -> Tuple[bool, int]:
    l_balanced, l_height = is_balanced_binary_tree_impl(tree.left) if tree.left else (True, 0)
    r_balanced, r_height = is_balanced_binary_tree_impl(tree.right) if tree.right else (True, 0)

    if not l_balanced or not r_balanced:
        return False, None

    if abs(l_height - r_height) > 1:
        return False, None

    return True, max(l_height, r_height) + 1

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    if not tree:
        return True

    balanced, _ = is_balanced_binary_tree_impl(tree)
    
    return balanced


def test(tree_arr: list, balanced: bool):
    tree = BinaryTreeNode.from_array(tree_arr)

    actual = is_balanced_binary_tree(tree)
    assert actual == balanced, f"For {tree} expected {balanced}, got {actual}"


if __name__ == '__main__':
    test([1], True)
    test([1,                  
             [3, [4]],        
             [2, [6], [12]],   
         ], True)
    test([1, [2, [3, [4, [5]]]]], False)

    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
