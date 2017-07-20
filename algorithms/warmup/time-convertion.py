#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/time-conversion

import sys

def timeConversion(s):
    # Complete this function
    i = s.split(':')
    if i[2].endswith('PM'):
        if int(i[0]) != 12:
            i[0] = '{}'.format(int(i[0]) + 12)
    elif int(i[0]) == 12:
        i[0] = '00'
    return '{:0>2}:{}:{:.2}'.format(*i)

s = input().strip()
result = timeConversion(s)
print(result)
