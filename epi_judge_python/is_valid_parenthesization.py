import sys
from test_framework import generic_test


OPEN = "{[("
CLOSE = "}])"


def index_of(c: str):
    try:
        return OPEN.index(c)
    except ValueError:
        return -1
    except Exception as e:
        raise e


def is_well_formed(s: str) -> bool:
    expected_close = []  # stack of close items

    for c in s:
        idx = index_of(c)
        if idx >= 0:
            expected_close.append(CLOSE[idx])
        elif expected_close and c == expected_close[-1]:
            expected_close.pop()
        elif c in CLOSE:
            return False

    return not expected_close


assert not is_well_formed("}{"), "}{ must be false"
assert not is_well_formed(")("), "}{ must be false"

if __name__ == '__main__':
    sys.exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
