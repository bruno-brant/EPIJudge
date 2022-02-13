from random import randint
from threading import Event, Thread
from time import sleep
from typing import Iterable, List


class Producer(Thread):
    def __init__(self, it: Iterable[int], shared_mem: List[int], my_event: Event, other_event: Event):
        super().__init__()
        self._iter = it
        self._shared_mem = shared_mem
        self._my_event = my_event
        self._other_event = other_event

    def run(self) -> None:
        for v in self._iter:
            self._my_event.wait()

            self._shared_mem.append(v)

            self._my_event.clear()
            self._other_event.set()

            if randint(1, 10) % 10 == 0:
                print(len(self._shared_mem))


def produce_array(array_range: int):
    store = []
    even_event = Event()
    odd_event = Event()
    odd = Producer(range(1, array_range+1, 2), store, odd_event, even_event)
    even = Producer(range(2, array_range+1, 2), store, even_event, odd_event)

    # Begin with odd
    odd_event.set()
    even_event.clear()

    even.start()
    odd.start()

    even.join()
    odd.join()

    return store


if __name__ == "__main__":
    sizes = [1, 10, 1000, 100_000]
    for size in sizes:
        for _ in range(10):
            values = produce_array(size)

            if len(values) != size:
                raise Exception(
                    f"Not enough entries in the array: expected {size}, got {len(values)}")

            for i, _ in enumerate(values):
                if values[i] != i + 1:
                    raise Exception(
                        f"Wrong entry at array position {i}: {values[i]}")

        print(f"Test {size} success.")
