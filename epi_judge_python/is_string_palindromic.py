from test_framework import generic_test


def is_palindrom_char(s: str) -> bool:
    assert len(s) == 1, f"expected a char, got {s}"
    assert s.lower() == s, f"s must be lower case: {s}"

    return ord('a') <= ord(s) <= ord('z')


def is_palindromic(s: str) -> bool:
    i = 0
    j = len(s) - 1

    while i < j:
        v_i = s[i].lower()
        v_j = s[j].lower()

        if not is_palindrom_char(v_i):
            i += 1
        elif not is_palindrom_char(v_j):
            j -= 1
        elif v_i != v_j:
            return False
        else:
            i += 1
            j -= 1

    return True


def test(s, expected: bool):
    actual = is_palindromic(s)

    assert actual == expected, f"{s}, expected {expected}, got {actual}"


if __name__ == '__main__':

    test("", True)
    test("a", True)
    test("ab", False)
    test("abc", False)
    test("aba", True)
    test("a a", True)

    print("Unit tests are done")

    exit(
        generic_test.generic_test_main('is_string_palindromic.py',
                                       'is_string_palindromic.tsv',
                                       is_palindromic))
