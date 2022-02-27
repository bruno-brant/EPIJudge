from typing import Generic, Set, Dict, List, TypeVar
from test_framework import generic_test

AdjacencyList = Dict[str, List[str]]

T = TypeVar("T")

class Queue(Generic[T]):
    def __init__(self, data: List[T]) -> None:
        self._data = data if data is not None else []

    def enqueue(self, elem: T) -> None:
        self._data.insert(0, elem)

    def dequeue(self) -> T:
        return self._data.pop()

    def is_empty(self) -> bool:
        return len(self._data) == 0

variations_cache = {}

def get_variations(w: str):
    if w in variations_cache:
        return variations_cache[w]

    variations_of_w = []
    
    for i in range(len(w)):
        for j in range(ord('a'), ord('z') + 1):
            var = w[0:i] + chr(j) + w[i+1:]
            if var != w:
                variations_of_w.append(var)

    variations_cache[w] = variations_of_w

    return variations_of_w


def transform_string(D: Set[str], s: str, t: str) -> int:
    D.remove(s)
    queue = Queue([(s, 0)])

    while not queue.is_empty():
        node, dist = queue.dequeue()

        for adj in get_variations(node):
            if adj not in D:
                continue

            if adj == t:
                return dist + 1

            D.remove(adj)
            queue.enqueue((adj, dist + 1))
    return -1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
