#!/usr/bin/python3
"""0-minoperations.py
"""


def minOperations(n):
    """
    This function calculates the minimum number of operations that cna be done
    """
    if n <= 1:
        return 0
    divisor = 2
    num_of_operations = 0
    while 1 < n:
        if n % divisor == 0:
            n = n / divisor
            num_of_operations += divisor
        else: 
            divisor += 1
            
    return num_of_operations