import functools
import sys
from typing import Optional

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# Input nodes are nonempty and the key at s is less than or equal to that at b.
def find_lca(tree: BstNode, s: BstNode, b: BstNode) -> Optional[BstNode]:
    browser = tree

    while True:
        if browser is None:
            return None

        if browser.data in [s.data, b.data]:
            return browser

        if s.data < browser.data < b.data:
            return browser

        browser = browser.left if s.data < browser.data else browser.right


@enable_executor_hook
def lca_wrapper(executor, tree, s, b):
    result = executor.run(
        functools.partial(find_lca, tree, must_find_node(tree, s),
                          must_find_node(tree, b)))
    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    sys.exit(
        generic_test.generic_test_main('lowest_common_ancestor_in_bst.py',
                                       'lowest_common_ancestor_in_bst.tsv',
                                       lca_wrapper))
