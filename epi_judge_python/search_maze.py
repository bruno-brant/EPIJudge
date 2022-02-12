import collections
import copy
import functools
from typing import Iterable, List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

Maze = List[List[int]]


class MazeRunner:
    """Process a maze"""

    def __init__(self, maze: Maze) -> None:
        self._maze = maze
        self._dimension_i = len(maze)
        self._dimension_j = len(maze[0])

    def __getitem__(self, coord: Coordinate):
        return self._maze[coord.x][coord.y]

    def __contains__(self, coord: Coordinate):
        return 0 <= coord.x < self._dimension_i and 0 <= coord.y < self._dimension_j

    def get_neighbors(self, coord: Coordinate) -> Iterable[Coordinate]:
        up = Coordinate(coord[0] - 1, coord[1])
        right = Coordinate(coord[0], coord[1] + 1)
        down = Coordinate(coord[0] + 1, coord[1])
        left = Coordinate(coord[0], coord[1] - 1)

        for i in [up, right, down, left]:
            if i in self and self[i] == WHITE:
                yield i

    def depth_first_search(self,
                           current: Coordinate,
                           e: Coordinate,
                           path: List[Coordinate],
                           visited: "set[Coordinate]") -> List[Coordinate]:

        visited.add(current)
        my_path = path + [current]

        for neighbor in self.get_neighbors(current):
            if neighbor in visited:
                continue

            if neighbor == e:
                return my_path + [neighbor]

            solution = self.depth_first_search(neighbor, e, my_path, visited)

            if solution is not None:
                return solution

        return None


def search_maze(maze: Maze, s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    runner = MazeRunner(maze)

    path = runner.depth_first_search(s, e, [], set())

    return path


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False

    return cur == (prev.x + 1, prev.y) or \
        cur == (prev.x - 1, prev.y) or \
        cur == (prev.x, prev.y + 1) or \
        cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


def test(maze, s, e, path):
    actual = search_maze(maze, s, e)
    assert path == actual, f"Expected {path}, got {actual}"


if __name__ == '__main__':
    # maze1 = [
    #     #  0      1      2      3
    #     [BLACK, BLACK, WHITE, BLACK],  # 0
    #     [BLACK, BLACK, WHITE, BLACK],  # 1
    #     [BLACK, BLACK, WHITE, BLACK],  # 2
    # ]

    # test(maze1, (0, 2), (2, 2), [(0, 2), (1, 2), (2, 2)])

    # maze2 = [
    #     #  0      1      2      3
    #     [WHITE, BLACK, BLACK, BLACK],  # 0
    #     [WHITE, WHITE, WHITE, BLACK],  # 1
    #     [BLACK, BLACK, WHITE, WHITE],  # 2
    # ]

    # test(maze2,
    #      (0, 0), (2, 3),
    #      [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (2, 3)])

    # maze3 = [
    #     #  0      1      2      3      4
    #     [BLACK, BLACK, WHITE, BLACK, BLACK],  # 0
    #     [BLACK, BLACK, WHITE, BLACK, BLACK],  # 1
    #     [WHITE, WHITE, WHITE, WHITE, WHITE],  # 2
    #     [BLACK, BLACK, WHITE, BLACK, BLACK],  # 3
    #     [BLACK, BLACK, WHITE, BLACK, BLACK],  # 4
    # ]

    # test(maze3, (2, 0), (2, 4), [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)])
    # test(maze3, (0, 2), (4, 2), [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)])

    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
