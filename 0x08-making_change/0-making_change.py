#!/usr/bin/python3
"""Making change module."""


def makeChange(coins, total):
    """Finds the minimum number of coins of total."""
    if total <= 0:
        return 0

    coins = sorted(coins, reverse=True)
    count = 0
    for coin in coins:
        while coin <= total and total > 0:
            total -= coin
            count += 1
    if total == 0:
        return count
    return -1
