#!/usr/bin/python3
"""coins module"""


def makeChange(coins, total):
    """calculates fewest coins to get total."""
    if total <= 0:
        return 0
    if coins == [] or coins is None:
        return -1
    coins.sort(reverse=True)
    index = 0
    value = 0
    count = 0
    while index < len(coins):
        value = value + coins[index]
        if value > total:
            if index < len(coins) - 1:
                value = value - coins[index]
                index = index + 1
            else:
                return -1
        elif value < total:
            count = count + 1
        elif value == total:
            count = count + 1
            return count
