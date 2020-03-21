"""
Problem: https://www.hackerrank.com/challenges/equality-in-a-array/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    num_dict = {}
    for num in arr: 
        if num in num_dict.keys(): #if there exists 
            num_dict[num] = num_dict.get(num, 0) + 1 
        else: 
            num_dict[num] = 1
    sorted_numdict = sorted(num_dict.items(), reverse=True, key=lambda kv: kv[1])
    print(num_dict)
    print(sorted_numdict)
    return (len(arr) - sorted_numdict[0][1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
