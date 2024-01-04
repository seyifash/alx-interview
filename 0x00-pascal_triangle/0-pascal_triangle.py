#!/usr/bin/python3
"""pascal triangle question"""

def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = [[1]]
    for _ in range(1, n):
        prev_row = triangle[-1]
        next_row = [1]
        for i in range(1, len(prev_row)):
            next_row.append(prev_row[i - 1] + prev_row[i])
        next_row.append(1)
        triangle.append(next_row)
    return triangle
