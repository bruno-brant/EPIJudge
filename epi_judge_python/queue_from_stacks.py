from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    def __init__(self) -> None:
        self._data = []

    def push(self, x: int):
        self._data.append(x)

    def pop(self):
        return self._data.pop()

    def __len__(self):
        return len(self._data)

    def __repr__(self) -> str:
        return repr(self._data)


class Queue:
    def __init__(self) -> None:
        self._enqueue = Stack()
        self._dequeue = Stack()

    def enqueue(self, x: int) -> None:
        self._enqueue.push(x)

    def dequeue(self) -> int:
        if not self._dequeue:
            while self._enqueue:
                self._dequeue.push(self._enqueue.pop())
        
        return self._dequeue.pop()



def queue_tester(ops):
    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_from_stacks.py',
                                       'queue_from_stacks.tsv', queue_tester))
