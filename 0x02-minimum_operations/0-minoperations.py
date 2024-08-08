#!/usr/bin/python3
"""This module contains a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file."""
from math import sqrt


def  minOperations(n):
    """This is a method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file."""
    if n <= 1:
        return 0
    factor = 2
    operations = 0

    while n > 1:
        while n % factor == 0:
            n //= factor
            operations += factor
        factor += 1

    return operations
