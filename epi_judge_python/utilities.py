from typing import Any, Callable, Generic, Iterable, List, TypeVar, Union


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

    def peek(self):
        return self.heap[0]

    def push(self, v: T):
        return self.__add__(v)

    def pop(self) -> T:
        if len(self) == 1:
            return self.heap.pop()

        value = self[0]

        self[0] = self.heap.pop()

        self._heapify(0)

        return value

    def __call__(self) -> T:
        return self.pop()

    def __add__(self, v: T) -> 'Heap':
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

    def __repr__(self) -> str:
        return repr(self.heap)

    def __str__(self) -> str:
        return str(self.heap)

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


test_max_heap([12, 5124, -2, 12, 2, 5, 7, 982, -1000])
test_max_heap([])
test_max_heap([0])


def test_min_heap(unordered: List[int]):
    ordered = sorted(unordered)

    heap = MinHeap[int]()

    for i in unordered:
        heap += i

    actual: List[str] = []
    while len(heap) > 0:
        actual.append(heap())

    assert actual == ordered, f"Expected {ordered}, got {actual}"


test_min_heap([12, 5124, -2, 12, 2, 5, 7, 982, -1000])
test_min_heap([])
test_min_heap([0])

TSlice = TypeVar("TSlice")


class Slice(Generic[TSlice]):
    def __init__(self, arr: Union[List[TSlice], 'Slice[TSlice]'], start: int = 0, end: int = None):
        end = end if end is not None else len(arr)

        if isinstance(arr, list):
            self._arr = arr
            self._start = start
            self._end = end
        elif isinstance(arr, Slice):
            self._arr = arr._arr
            self._start = arr._start + start
            self._end = arr._start + end
        else:
            raise ValueError("Invalid arr")

    def index(self, value):
        for i, v in enumerate(self._arr[self._start:self._end]):
            if v == value:
                return i

        return -1

    def __getitem__(self, idx: 0) -> TSlice:
        if idx > (self._end - self._start):
            raise IndexError(idx)

        return self._arr[self._start + idx]

    def __len__(self):
        return self._end - self._start

    def __repr__(self):
        return repr(self._arr[self._start:self._end])

    def __str__(self):
        return str(self._arr[self._start:self._end])


assert Slice([0, 1, 2, 3], 2)[1] == 3
assert Slice([0, 1], 1)[0] == 1
assert Slice(Slice([0, 1, 2, 3, 4], 2, 3), 1)[0] == 3
assert repr(Slice([0, 1, 2], 0)) == "[0, 1, 2]"
