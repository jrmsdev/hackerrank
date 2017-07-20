#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/diagonal-difference

import sys

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

def rdiag (rlen, r, secondary = False):
    s = 0
    i = 0
    j = 0
    if secondary:
        j = rlen - 1
    for n in range (rlen):
        s += r[i][j]
        if secondary:
            i += 1
            j -= 1
        else:
            i += 1
            j += 1
    return s

print (abs ((rdiag (n, a) - rdiag (n, a, True))))
