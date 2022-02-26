from typing import Set, Dict, List

from test_framework import generic_test

AdjacencyList = Dict[str, List[str]]


def is_within_distance(w1: str, w2: str, max_dist: int) -> bool:
    dist = 0
    for c1, c2 in zip(w1, w2):
        if c1 != c2:
            dist += 1
            if dist > max_dist:
                return False
    return True


def build_graph(D: Set[str]) -> AdjacencyList:
    g: AdjacencyList = {}

    while D:
        node = D.pop()

        if node not in g:
            g[node] = []

        for w in D:
            if not is_within_distance(node, w, 1):
                continue
            
            g[node].append(w)

            if w not in g:
                g[w] = [node]
            else:
                g[w].append(node)

    return g


class Queue:
    def __init__(self, data: List[str]) -> None:
        self._data = data if data is not None else []

    def enqueue(self, w: str) -> None:
        self._data.insert(0, w)

    def dequeue(self) -> str:
        return self._data.pop()

    def is_empty(self) -> bool:
        return len(self._data) == 0


def transform_string(D: Set[str], s: str, t: str) -> int:
    g = build_graph(D)

    parent: Dict[str, str] = {s: None}
    to_process = Queue([s])
    discovered = set([s])

    while not to_process.is_empty():
        node = to_process.dequeue()

        for child in g[node]:
            if child in discovered:
                continue

            discovered.add(child)
            to_process.enqueue(child)
            parent[child] = node

    distance = 0
    current = t
    while current != s:
        current = parent.get(current, -1)
        if current == -1:
            return -1
        distance += 1

    return distance


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
