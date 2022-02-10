from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:

    available_letters = {}
    
    for char in [chr(char).lower() for char in range(ord('0'), ord('z'))]:
        available_letters[char] = 0    
    
    for char in magazine_text:
        if char in available_letters:
            available_letters[char] += 1

    for char in letter_text:
        if char in available_letters:
            available_letters[char] -= 1
            if available_letters[char] < 0:
                return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
