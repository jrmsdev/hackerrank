#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/py-set-mutations

_ = input ().strip ()
A = set (map (int, input ().strip ().split ()))
N = int (input ().strip ())

for _ in range (N):
    cmd = input ().strip ().split ()[0]
    s = set (map (int, input ().strip ().split ()))
    if cmd == 'intersection_update':
        A.intersection_update (s)
    elif cmd == 'update':
        A.update (s)
    elif cmd == 'symmetric_difference_update':
        A.symmetric_difference_update (s)
    elif cmd == 'difference_update':
        A.difference_update (s)

print (sum (A))
