from typing import Callable, Optional, Tuple
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

Comparer = Callable[[int, Optional[int], Optional[int]], int]



def is_binary_tree_bst(tree: BinaryTreeNode, min: int = None, max: int = None) -> bool:
    if tree == None:
        return True

    if min != None and tree.data < min:
        return False
    
    if max != None and tree.data > max:
        return False
    
    if tree.left:
        if not is_binary_tree_bst(tree.left, min, tree.data):
            return False

    if tree.right:
        if not is_binary_tree_bst(tree.right, tree.data, max):
            return False

    return True

def test(tree, is_binary):
    tree_ = BinaryTreeNode.from_array(tree)
    actual = is_binary_tree_bst(tree_)

    assert actual == is_binary, f"Tree {tree}, expected {is_binary}, got {actual}"


if __name__ == '__main__':
    test([1], True)
    test([1, [-1], [2]], True)
    test([1, [-1, [5]]], False)

    a = [-22,
         [-24,
          None,
          [-23]],
         [-17,
          [-24],
             None]
         ]
    test(a, False)
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
