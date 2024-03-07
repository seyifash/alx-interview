#!/usr/bin/python3
"""
A method that calculates the perimeter of an island
"""


def island_perimeter(grid):
    """This method calcultes the island of a perimeter"""
    if grid == None or len(grid) == 0:
        return 0
    result = 0

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == 1:
                result += 4

                if i > 0 and grid[i - 1][j] == 1:
                    result -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    result -= 2

    return result
