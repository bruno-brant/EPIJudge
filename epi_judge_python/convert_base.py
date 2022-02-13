from math import factorial
from test_framework import generic_test

VALUE_TO_DIGIT = [str(i) for i in range(0, 10)] + [chr(i) for i in range(ord('A'), ord('F') + 1)]

TABLE = []

for i in range(0, 256):
    if chr(i) not in VALUE_TO_DIGIT:
        TABLE.append(0)
    else:
        TABLE.append(VALUE_TO_DIGIT.index(chr(i)))
    

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    value = parse_num(num_as_string, b1)
    return serialize_num(value, b2)

def parse_num(num_as_string: str, b1: int) -> int:
    value = 0
    magnitude = 1

    factor = 1
    if num_as_string[0] == '-':
        factor = -1
        num_as_string = num_as_string[1:]

    for c in reversed(num_as_string):
        value += TABLE[ord(c)] * magnitude
        magnitude *= b1

    return value * factor

def serialize_num(num: int, b1: int) -> str:
    if num == 0:
        return '0'
        
    chars = []
    
    is_negative = False
    
    if num < 0:
        is_negative = True
        num = -num

    while num > 0:
        value = num % b1
        chars.append(VALUE_TO_DIGIT[value])

        num -= value
        num = num // b1

    if is_negative:
        chars.append('-')

    return ''.join(reversed(chars))


def test(num_as_string: str, b1: int, b2: int, expected: str):
    actual = convert_base(num_as_string, b1, b2)
    assert expected == actual, f"Convert {num_as_string} in {b1} to {b2}, expected {expected}, got {actual}"

def test_parse(num_as_string: str, b1: int, expected: int):
    actual = parse_num(num_as_string, b1)
    assert expected == actual, f"Parse {num_as_string} in {b1}, expected {expected}, got {actual}"

def test_serialize(value: int, b1: int, expected: str):
    actual = serialize_num(value, b1)
    assert expected == actual, f"Serialize {value} to {b1}, expected {expected}, got {actual}"


if __name__ == '__main__':
    test_parse('-1', 10, -1)
    test_parse('-F', 16, -15)
    test_parse('1', 2, 1)
    test_parse('1', 10, 1)
    test_parse('2', 10, 2)
    test_parse('10', 2, 2)
    test_parse('5', 10, 5)
    test_parse('A', 16, 10)
    test_parse('A1', 16, 10 * 16 + 1)
    test_parse('AF', 16, 10 * 16 + 15)

    test_serialize(1, 2, '1')
    test_serialize(16, 16, '10')
    test_serialize(8, 2, '1000')
    test_serialize(16, 2, '10000')
    test_serialize(-16, 2, '-10000')
    test_serialize(6, 2, '110')
    test_serialize(3, 2, '11')
    test_serialize(-3, 2, '-11')

    test('0', 6, 6, '0')
    
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
