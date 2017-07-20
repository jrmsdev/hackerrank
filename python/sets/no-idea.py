#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/no-idea

n, m = map (int, input ().strip ().split ())
arr = list (map (int, input ().strip ().split ()))
A = set (map (int, input ().strip ().split ()))
B = set (map (int, input ().strip ().split ()))

h = 0
for i in arr:
    if i in A:
        h += 1
    elif i in B:
        h -= 1

print (h)
