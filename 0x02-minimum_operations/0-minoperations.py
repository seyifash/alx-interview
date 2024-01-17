#!/usr/bin/python3
""" counts the minimum operations
"""


def minOperations(n):
    """ this function calculates the minimum number of operations that cna be done
    """
    if n <= 1:
        return 0
    divisor = 2
    num_of_operations = 0
    while n > 1:
        if n % divisor == 0:
            n = n / divisor
            num_of_operations = num_of_operations + divisor
        else: 
            divisor += 1
            
    return num_of_operations