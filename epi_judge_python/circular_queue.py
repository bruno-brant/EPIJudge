from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity: int) -> None:
        if capacity == 0:
            raise Exception("Capacity is zero")

        self._data = [None] * capacity
        self._start = 0
        self._end = 0

    def enqueue(self, x: int) -> None:
        next_end = self._next_index(self._end)

        if next_end == self._start:
            # We must increase storage
            self._increase_storage()
            self.enqueue(x)
        else:
            self._data[self._end] = x
            self._end = next_end

    def dequeue(self) -> int:
        x = self._data[self._start]
        self._data[self._start] = None

        self._start = self._next_index(self._start)

        return x

    def size(self) -> int:
        """The current number of items (depth) of the queue."""
        if self._end < self._start:
            return self._end + (len(self._data) - self._start)

        return self._end - self._start

    def _increase_storage(self):
        """Doubles storage"""
        old_size = self.size()
        old_data = self._data
        self._data = [None] * len(self._data) * 2
    
        # Copy over
        for i in range(old_size):
            self._data[i] = old_data[(self._start + i) % len(old_data)]

        self._end = old_size
        self._start = 0

    def _next_index(self, idx: int):
        return (idx + 1) % len(self._data)


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
