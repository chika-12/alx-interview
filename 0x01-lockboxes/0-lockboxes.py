#!/usr/bin/python3
"""Lock boxes"""


def canUnlockAll(boxes):
    visited = set([0])
    len_of_box = len(boxes)
    stack = [0]

