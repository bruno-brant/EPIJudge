import functools
from typing import List, Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class Path:
    def __init__(self) -> None:
        self.path: set[int] = set()

    def __add__(self, node: BinaryTreeNode):
        self.path.add(id(node))
        return self

    def __contains__(self, node: BinaryTreeNode):
        return id(node) in self.path


def lca(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    if node0 is None or node1 is None:
        return None

    if node0 is node1:
        return node0

    path_node0 = Path() + node0
    path_node1 = Path() + node1

    while True:
        if node0.parent:
            node0 = node0.parent
            path_node0 += node0
            if node0 in path_node1:
                return node0

        if node1.parent:
            node1 = node1.parent
            path_node1 += node1
            if node1 in path_node0:
                return node1

        if not node0.parent and not node1.parent:
            return None


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
