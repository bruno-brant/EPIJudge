import collections
import sys

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))

NullRect = Rect(0, 0, -1, -1)

class Rectangle:
    def __init__(self, r: Rect) -> None:
        self.x1 = r.x
        self.x2 = r.x + r.width
        self.y1 = r.y
        self.y2 = r.y + r.height

    def __repr__(self):
        return f"x1={self.x1} x2={self.x2} y1={self.y1} y2={self.y2}"

def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    # order by X
    r1_, r2_ = map(Rectangle, sorted([r1, r2], key=lambda r: r.x))
    
    # if the distance between r2 and r1 is larger than r1.width, stop
    if r1_.x2 < r2_.x1:
        return NullRect

    ri_x1 = r2_.x1
    ri_x2 = min([r1_.x2, r2_.x2])

    # order by Y
    r1_, r2_ = map(Rectangle, sorted([r1, r2], key=lambda r: r.y))

    # if the distance between r2 and r1 is larger than r1.height, stop
    if r1_.y2 < r2_.y1:
        return NullRect

    ri_y1 = r2_.y1
    ri_y2 = min([r1_.y2, r2_.y2])

    return Rect(ri_x1, ri_y1, ri_x2 - ri_x1, ri_y2 - ri_y1)


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    
    return value


if __name__ == '__main__':
    sys.exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
