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
    letter: int = 1
    copy: int = 1
    op: int = 1
    nim: int = 100000000000000
    factors: List[int] = []
    if n == 0 or n == 1:
        return 0

    for factor in range(2, n):
        if n % factor == 0:
            factors.append(factor)
    # print (factors)
    for num in factors:
        # print(num)
        if (num < nim):
            nim = num
    # print(nim)

    while letter <= n:
        if letter == n:
            return op
        # paste until reaching the nim
        if letter < nim:
            op += 1
            letter += copy
            # if (n % (copy + letter) == 0 and copy != 1 and copy != 0):
            # print(f"{copy + letter} akafay copy: {copy} letter: {letter}")
            #     op += 1
            #     letter += copy
            # else:
            #     print(f"no akafay copy: {copy} letter: {letter}")
            #     op += 1
            #     copy += letter
        # paste
        if letter in factors:

            op += 1
            copy = letter
            op += 1
            letter += copy
            # print(f"copy-paste:  paste letter: {letter} copy: {copy}")

        else:
            # print(f"paste letter: {letter} copy: {copy}")
            # op += 1
            # copy = letter
            op += 1
            letter += copy
    return 0
