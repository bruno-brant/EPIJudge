from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    data = []
    max_stack = []

    def empty(self) -> bool:
        return len(self.data) == 0

    def max(self) -> int:
        if not self.max_stack:
            return None

        return self.data[self.max_stack[-1]]

    def pop(self) -> int:
        pop_idx = len(self.data) - 1

        if pop_idx == self.max_stack[-1]:
            self.max_stack.pop()

        return self.data.pop()

    def push(self, x: int) -> None:
        self.data.append(x)

        if self.max() == None or self.max() <= x:
            self.max_stack.append(len(self.data) - 1)

def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure(f'Unexpected IndexError exception on {op}, {arg} ')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
