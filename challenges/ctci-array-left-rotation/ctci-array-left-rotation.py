#!/usr/bin/env python3

from collections import deque

def rotate (a, d):
    q = deque (a)
    q.rotate (d * -1)
    return [n for n in q]

_, d = list (map (int, input ().strip ().split ()))
arr = list (map (int, input ().strip ().split ()))

r = rotate (arr, d)
print (' '.join (map (str, r)))
