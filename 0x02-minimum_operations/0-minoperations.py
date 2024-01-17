#!/usr/bin/python3
""" counts the minimum operations
"""


def minOperations(n):
    """ this function calculates the minimum nuber of operations that cna be done
    """
    if n <= 1:
        return 0
    
    current_length = "H"
    numberOfOp = 0
    
    while len(current_length) < n:
        if n % len(current_length) == 0:
            current_length = current_length + current_length
            numberOfOp += 2
        else:
            current_length += current_length
            numberOfOp += 1
    
    return numberOfOp 
