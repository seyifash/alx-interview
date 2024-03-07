#!/usr/bin/python3
"""
A method to calculate minimum operations
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
            print("value of n is: {}".format(n))
            num_of_operations += divisor
            print("num of operations: {}".format(num_of_operations))
        else:
            divisor += 1
            print("divisor in else: {}".format(divisor))
    return num_of_operations
