#!/usr/bin/python3
""" Minimum operation"""


def minOperations(n):
    if n < 1:
        return 0
    factor = 2
    opp = 0

    while n > 1:
        while n % factor == 0:
            opp += factor
            n //= factor
        factor += 1
    return opp
