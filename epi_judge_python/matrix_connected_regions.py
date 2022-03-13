from typing import Iterator, List

from test_framework import generic_test


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __hash__(self) -> int:
        return hash(self.x) ^ hash(self.y)


class Image:
    def __init__(self, image: List[List[bool]]) -> None:
        self._image = image

    def __getitem__(self, p: Point) -> bool:
        return self._image[p.x][p.y]

    def __setitem__(self, p: Point, color: bool):
        self._image[p.x][p.y] = color

    def neighbors(self, p: Point) -> Iterator[Point]:
        if (p.x + 1) < len(self._image):
            yield Point(p.x + 1, p.y)

        if (p.y + 1) < len(self._image[p.x]):
            yield Point(p.x, p.y + 1)

        if (p.x - 1) >= 0:
            yield Point(p.x - 1, p.y)

        if (p.y - 1) >= 0:
            yield Point(p.x, p.y - 1)


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    img = Image(image)
    start = Point(x, y)

    stack = [start]
    visited = set(stack)
    color = img[start]

    # Perform DFS to find all elements
    while stack:
        p = stack.pop()

        # flips color at point
        img[p] = not color

        for neighbor in img.neighbors(p):
            if img[neighbor] != color:
                continue

            if neighbor not in visited:
                visited.add(p)
                stack.append(neighbor)


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
