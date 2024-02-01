#!/usr/bin/python3
""" Method to check if a list of number is valis utf-8
"""


def validUTF8(data):
    """checks if list contains valid utf-8
    """
    def isValid(byte):
        mask = 1 << (8 - 1)
        i = 0
        while byte & mask:
            mask >>= 1
            i += 1
        return i
    i = 0
    while i < len(data):
        j = isValid(data[i])
        k = i + j - ( j != 0)
        i += 1
        if j == 1 or j > 4 or k >= len(data):
            return False
        while i < len(data) and i <= k:
            cur = isValid(data[i])
            if cur != 1:
                return False
            i += 1
    return True
