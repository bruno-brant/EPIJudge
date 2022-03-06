import functools
from typing import Optional, Set

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def get_depth(node: BinaryTreeNode):
    depth = 0

    while node.parent:
        node = node.parent
        depth += 1

    return depth


def lca(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    if node0 is None or node1 is None:
        return None

    if node0 is node1:
        return node0

    depth0, depth1 = get_depth(node0), get_depth(node1)

    node0, node1 = (node0, node1) if depth0 < depth1 else (node1, node0)

    diff = abs(depth0 - depth1)

    # make same depth
    for _ in range(diff):
        node1 = node1.parent

    while node0 != node1:
        node0 = node0.parent
        node1 = node1.parent

    return node0


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
