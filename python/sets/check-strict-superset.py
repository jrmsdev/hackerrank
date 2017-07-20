#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/py-check-strict-superset

A = set (input ().strip ().split ())
n = int (input ().strip ())

x = set ()
lenA = len (A)

for _ in range (n):
    s = set (input ().strip ().split ())
    if lenA > len (s) and A.issuperset (s):
        x.add (True)
    else:
        x.add (False)

print (all (x))
