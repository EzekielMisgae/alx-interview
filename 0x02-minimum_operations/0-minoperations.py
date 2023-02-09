#!/usr/bin/python3
"""
Gets the minimum operations
"""


def minOperations(n):
    """ calculates the fewest number of operations
    needed to result in n H charaters """
    if n <= 0:
        return 0
    operations = 0
    while n != 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n -= 1
        operations += 1
    return operations
