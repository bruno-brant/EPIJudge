from test_framework import generic_test


def look_and_say(n: int) -> str:
    if n == 0:
        return ""

    if n == 1:
        return "1"

    term = "1"

    for _ in range(1, n):
        previous_term = term
        term = ""
        last_digit = previous_term[0]
        count = 1

        for digit in previous_term[1:]:
            if digit != last_digit:
                term += f"{count}{last_digit}"
                count = 1
                last_digit = digit
            else:
                count += 1
                
        term += f"{count}{last_digit}"
    return term


sequence = [1, 11, 21, 1211, 111221, 312211, 13112221]
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
