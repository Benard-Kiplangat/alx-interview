#!/usr/bin/python3
"""
Pascal_triangle function:
    param: n <number>
"""


def pascal_triangle(n):
    """
    The function that returns a pascal triangle
    """
    if n <= 0:
        return []
    p_triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(len(p_triangle[i - 1]) - 1):
            row.append(p_triangle[i - 1][j] + p_triangle[i - 1][j + 1])
        row.append(1)
        p_triangle.append(row)
    return p_triangle
