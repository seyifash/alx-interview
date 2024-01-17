#!/usr/bin/python3
""" counts the minimum operations
"""


def minOperations(n):
    """ this function calculates the minimum nuber of operations that cna be done
    """
    if not isinstance(n, int):
        return 0
    
    text1 = "H"
    numberOfOp = 0
    
    while len(text1) < n:
        if n % len(text1) == 0:
            copy = text1
            text1 = copy + text1
            numberOfOp += 2
        else:
            text1 = copy + text1
            numberOfOp += 1
    
    return numberOfOp 
