#!/usr/bin/env python3

from itertools import accumulate

arr = [7, 6, 4, 3, 2, 3]
print (arr)

count = [0 for _ in range (9)]
print ('C0:', count)

for n in arr:
    count[n] += 1
print ('C1:', count)

count = list (accumulate (count))
print ('C2:', count)

outarr = [None for _ in range (9)]
print ('O0:', outarr)

for n in arr:
    outarr[count[n]] = n
    count[n] -= 1 # allow duplicates
print ('O1:', outarr)

arr = [n for n in outarr if n is not None]
print (arr)
