from test_framework import generic_test


def can_form_palindrome(s: str) -> bool:
    needs_pair = set()

    for i in s:
        if i not in needs_pair:
            needs_pair.add(i)
        else:
            needs_pair.remove(i)

    if len(s) % 2 == 1: # odd
        return len(needs_pair) <= 1
    else:               # even
        return len(needs_pair) == 0

    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
