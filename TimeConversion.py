"""
Problem: https://www.hackerrank.com/challenges/time-conversion/problem
"""

#!/bin/python3

import os
import sys
import re #to verify form 
from datetime import datetime

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    input_format = re.match("^(0[0-9]|1[0-2]):[0-5][0-9]:[0-5][0-9][AP]M$", s) 
    if not input_format:
        return s
    daytime = s[-2]#get 2nd most right to either A or P 
    timeonly = s[:-2] # do not get the PM or AM 
    hr, minsec = timeonly.split(":", 1) #split the hr 
    if daytime == 'A' and hr == '12':  
        return '00:' +minsec   
    elif daytime == 'P' and hr != '12':
        return str(int(hr) + 12) + ":" + minsec
    return timeonly 

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
