"""
Problem: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    cloud = 0  
    while cloud + 3 < len(c): 
        if c[cloud] == 0: 
            if c[cloud+2] == 0: 
                cloud += 2 #jumps 1 step 
            else: 
                cloud += 1 #jumps 2 steps
            jumps += 1 
    jumps += 1 #takes 1 2-step jump to final  
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
