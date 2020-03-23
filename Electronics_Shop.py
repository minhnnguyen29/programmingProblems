"""
Problem: https://www.hackerrank.com/challenges/electronics-shop/problem
"""

#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    total = 0 
    if len(keyboards) <= len(drives):
        total = findTotal(drives, keyboards, b)
    else: 
        total = findTotal(keyboards, drives, b)
    return total

def findTotal(outerloop, innerloop, b):
    total = -1 #default, that could be spent (in case can't be updated, can't buy anything)
    for i in range(len(outerloop)): 
        for j in range(len(innerloop)):
            if outerloop[i] + innerloop[j] <= b: 
                total = max(total, outerloop[i] + innerloop[j])
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
