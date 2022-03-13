import sys
from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    if n < 2:
        return []

    sieve = [True] * (n + 1)

    for i in range(2, n + 1):
        if sieve[i]:
            for j in range(i * 2, n + 1, i):
                sieve[j] = False
        
    primes = []
    for i in range(2, len(sieve)):
        if sieve[i]:
            primes.append(i)

    return primes


if __name__ == '__main__':
    sys.exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
