from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


class End:
    pass


end = End()


def depth_search_right_first(tree: BinaryTreeNode):

    s = [tree]

    while s:
        e = s.pop()

        if e is None:
            yield None
        else:
            yield e.data
            s.insert(0, e.right)
            s.insert(0, e.left)

    yield end


def depth_search_left_first(tree: BinaryTreeNode):
    s = [tree]

    while s:
        e = s.pop()

        if e is None:
            yield None
        else:
            yield e.data
            s.insert(0, e.left)
            s.insert(0, e.right)

    yield end


def is_symmetric(tree: BinaryTreeNode) -> bool:
    if tree is None:
        return True

    left_it = depth_search_left_first(tree.left)
    right_it = depth_search_right_first(tree.right)

    while True:
        left = next(left_it)
        right = next(right_it)

        if left != right:
            return False

        if left == end and right == end:
            return True


if __name__ == '__main__':
    is_symmetric(BinaryTreeNode.from_array([None]))
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
