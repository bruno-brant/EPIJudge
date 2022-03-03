from typing import Generic, TypeVar
from test_framework import generic_test

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._data = []

    def push(self, value: T) -> None:
        self._data.append(value)

    def pop(self) -> T:
        return self._data.pop()


def evaluate(expression: str) -> int:
    expressions = expression.split(',')

    s = Stack[int]()

    for expression in expressions: 
        if expression == '+':
            s.push(s.pop() + s.pop())
        elif expression == '-':
            operand_2 = s.pop()
            operand_1 = s.pop()

            s.push(operand_1 - operand_2)
        elif expression == '*':
            s.push(s.pop() * s.pop())
        elif expression == '/':
            operand_2 = s.pop()
            operand_1 = s.pop()

            s.push(operand_1 // operand_2)
        else:
            s.push(int(expression))

    return s.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
