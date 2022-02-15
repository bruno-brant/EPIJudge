from typing import Any, Callable, Generic, Iterable, List, TypeVar


def cross(__iter1: Iterable, __iter2: Iterable):
    """Cross join of multiple Iterables"""

    for i in __iter1:
        for j in __iter2:
            yield (i, j)


T = TypeVar("T")


class Heap(Generic[T]):
    def __init__(self, dominates: Callable[[T, T], bool]) -> None:
        self.heap: List[T] = []
        self._dominates = dominates

    def __call__(self, *args: Any, **kwds: Any) -> T:
        if len(self) == 1:
            return self.heap.pop()

        value = self[0]

        self[0] = self.heap.pop()

        self._heapify(0)

        return value

    def __add__(self, v: T) -> 'MaxHeap':
        self.heap.append(v)
        self._bubble_up(len(self.heap) - 1)
        return self

    def __getitem__(self, index: int) -> T:
        return self.heap[index]

    def __setitem__(self, index: int, value: T):
        self.heap[index] = value

    def __len__(self):
        return len(self.heap)

    def _heapify(self, index: int):
        m = index

        left_idx = self._left(index)
        if left_idx:
            m = left_idx if self._dominates(self[left_idx], self[m]) else m

        right_idx = self._right(index)
        if right_idx:
            m = right_idx if self._dominates(self[right_idx], self[m]) else m

        if m == index:
            return

        self[index], self[m] = self[m], self[index]
        self._heapify(m)

    def _bubble_up(self, child_idx):
        parent_idx = self._parent(child_idx)

        if parent_idx is None:
            return

        if self._dominates(self[child_idx], self[parent_idx]):
            self[child_idx], self[parent_idx] = self[parent_idx], self[child_idx]

        self._bubble_up(parent_idx)

    def _right(self, index: int) -> int:
        k = index * 2
        return k if k < len(self) else None

    def _left(self, index: int) -> int:
        k = index * 2 + 1
        return k if k < len(self) else None

    def _parent(self, index: int) -> int:
        if index == 0:
            return None

        return index // 2

    def peek(self):
        return self.heap[0]


class MinHeap(Heap[T]):
    def __init__(self) -> None:
        def dominates(x: T, y: T) -> bool:
            return x < y

        super().__init__(dominates)


class MaxHeap(Heap[T]):
    def __init__(self) -> None:
        def dominates(x: T, y: T) -> bool:
            return x > y

        super().__init__(dominates)


def test_max_heap(unordered: List[int]):
    ordered = list(reversed(sorted(unordered)))

    heap = MaxHeap[int]()

    for i in unordered:
        heap += i

    actual: List[str] = []
    while len(heap) > 0:
        actual.append(heap())

    assert actual == ordered, f"Expected {ordered}, got {actual}"

def test_min_heap(unordered: List[int]):
    ordered = sorted(unordered)

    heap = MinHeap[int]()

    for i in unordered:
        heap += i

    actual: List[str] = []
    while len(heap) > 0:
        actual.append(heap())

    assert actual == ordered, f"Expected {ordered}, got {actual}"


if __name__ == '__main__':
    test_max_heap([12, 5124, -2, 12, 2, 5, 7, 982, -1000])
    test_max_heap([])
    test_max_heap([0])

    test_min_heap([12, 5124, -2, 12, 2, 5, 7, 982, -1000])
    test_min_heap([])
    test_min_heap([0])
