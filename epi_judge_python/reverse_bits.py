import sys
from test_framework import generic_test

lookup = {
    0b0000: 0b0000,  # 0
    0b0001: 0b1000,  # 1
    0b0010: 0b0100,  # 2
    0b0011: 0b1100,  # 3
    0b0100: 0b0010,  # 4
    0b0101: 0b1010,  # 5
    0b0110: 0b0110,  # 6
    0b0111: 0b1110,  # 7
    0b1000: 0b0001,  # 8
    0b1001: 0b1001,  # 9
    0b1010: 0b0101,  # 10
    0b1011: 0b1101,  # 11
    0b1100: 0b0011,  # 12
    0b1101: 0b1011,  # 13
    0b1110: 0b0111,  # 14
    0b1111: 0b1111,  # 15
}


def reverse_bits(x: int) -> int:
    n = 0

    for starting_bit in range(0, 64, 4):
        part = (x >> starting_bit) & 0xF
        n = n | (lookup[part] << (60 - starting_bit))

    return n


if __name__ == '__main__':
    sys.exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
