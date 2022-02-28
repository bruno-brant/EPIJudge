from test_framework import generic_test


def reverse(x: int) -> int:
    is_negative =  -1 if x < 0 else 1
        
    r =  int(''.join(reversed(str(abs(x)))))

    return is_negative * r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
