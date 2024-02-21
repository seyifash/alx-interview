#!/usr/bin/python3
"""
rotateing the matrix by 90 degrees
"""


def rotate_2d_matrix(matrix):
    """A method that rotates the matrix by swapping them"""
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

