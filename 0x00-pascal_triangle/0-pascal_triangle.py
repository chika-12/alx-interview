#!/usr/bin/python3
"""Pascal triangle on display"""


def pascal_triangle(n):
    """Pascal function"""
    if n <= 0:
        return []

    triangle = [[1]]

    for index in range(1, n):
        row = [1]
        for idx in range(1, index):
            row.append(triangle[index - 1][idx - 1] + triangle[index - 1][idx])
        row.append(1)
        triangle.append(row)
    return triangle
