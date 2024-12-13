#!/usr/bin/python3
"""Prime game module."""


def SieveOfEratosthenes(n):
    sieve = [True] * (n + 1)
    p = 2
    sieve[0] = sieve[1] = False
    while (p * p <= n):
        if (sieve[p]):
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1
    return sieve


def isWinner(x, nums):
    """A fumction that returns the winner of the prime game."""
    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = SieveOfEratosthenes(max_num)
    prime_count = [0] * (max_num + 1)

    player1 = 'Maria'
    player2 = 'Ben'
    p1 = 0
    p2 = 0
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    for n in nums:
        primes_to_n = prime_count[n]
        if primes_to_n % 2 == 1:
            p1 += 1
        else:
            p2 += 1

    if p1 > p2:
        return player1
    elif p1 < p2:
        return player2
    else:
        return None
