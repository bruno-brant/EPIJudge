from queue import Queue
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if not tree:
        return []

    q_insert: Queue[BinaryTreeNode] = Queue()
    q_remove: Queue[BinaryTreeNode] = Queue()

    q_remove.put(tree)

    result: List[List[int]] = []
    level = 0

    # BFS
    while not q_remove.empty():
        result.append([])
        
        while not q_remove.empty():
            parent = q_remove.get()
            result[level].append(parent.data)

            if parent.left:
                q_insert.put(parent.left)
            
            if parent.right:
                q_insert.put(parent.right)

        q_insert, q_remove = q_remove, q_insert
        level += 1

    return result

def test(_input, expected):
    tree = BinaryTreeNode.from_array(_input)
    actual = binary_tree_depth_order(tree)
    assert expected == actual, f"Expected: {expected}, got {actual}"

if __name__ == '__main__':
    test([1], [[1]])
    test([1, [2], [3]], [[1], [2, 3]])

    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
