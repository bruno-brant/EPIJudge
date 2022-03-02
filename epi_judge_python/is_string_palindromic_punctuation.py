from test_framework import generic_test
import is_string_palindromic as palindrome 

def is_palindrome(s: str) -> bool:
    return palindrome.is_palindromic(s)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
