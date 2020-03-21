"""
Problem: https://www.hackerrank.com/challenges/repeated-string/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    number_a = s.count('a')#count total a in string s 
    if n == 0 or len(s) == 0: 
        return 0 
    total_a = 0 
    repeats = int(n/len(s))  
    remainder = n%len(s)
    remainder_a = s[:remainder].count('a')
    total_a = repeats*number_a + remainder_a 
    return total_a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
