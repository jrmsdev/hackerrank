#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/zipped

n, x = input().strip().split(' ')
n, x = [int(n), int(x)]

total = []

for i in range (x):
    r = []
    for j in input().strip().split(' '):
        r.append (float (j))
    total.append (r)

for u in zip (*total):
    s = 0
    for i in u:
        s += i
    print (s / x)
