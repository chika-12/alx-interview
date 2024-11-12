#!/usr/bin/python3
"""Lock boxes"""


def canUnlockAll(boxes):
    visited = set([0])
    len_of_box = len(boxes)
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key not in visited and key < len_of_box:
                visited.add(key)
                stack.append(key)

    if len(visited) == len_of_box:
        return True
    else:
        return False
