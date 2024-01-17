#!/usr/bin/python3
""" counts the minimum operations
"""


def minOperations(n):
    """ this function calculates the minimum number of operations that cna be done
    """
    if n == 1:
        return 0

    operations = 0
    current_h = 1
    clipboard = 0

    while current_h < n:
        if n % current_h == 0:
            # If current_h is a divisor of n, use the copy all and paste operation
            clipboard = current_h
            operations += 2

        current_h += clipboard
        operations += 1

    return operations if current_h == n else 0