#!/usr/bin/python3
"""Pascal triangle on display"""


def pascal_triangle(n):
    """Pascal function"""
    if n <= 0:
        return []

    pascal = [[1]]
    for index in range(1, n):
        row = [1]
        for idx in range(1, index):
            row.append(pascal[index - 1][idx - 1] + pascal[index - 1][idx])
        row.append(1)
        pascal.append(row)

    return pascal
