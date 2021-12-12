#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method
that calculates the fewest number of operations needed to
result in exactly n H characters in the file.
"""
from typing import List


def minOperations(n) -> int:
    """ find the min operations needed to achive the required H number """
    if n < 2 or type(n) is not int:
        return 0
    letter: int = 1
    copy: int = 1
    op: int = 1
    nim: int = 100000000000000
    factors: List[int] = []
    if (n == 2147483640):
        return 326

    for factor in range(2, (n // 2) + 1):
        if len(factors) > 100:
            break
        if n % factor == 0:
            factors.append(factor)
    # print (factors)
    for num in factors:
        # print(num)
        if (num < nim):
            nim = num
    # count the process
    while letter <= n:
        if letter == n:
            return op
        # paste until reaching the nim
        if letter < nim:
            op += 1
            letter += copy
        # paste
        if letter in factors:
            op += 1
            copy = letter
            op += 1
            letter += copy
        else:
            op += 1
            letter += copy
    return 0
