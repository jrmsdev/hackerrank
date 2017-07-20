#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/py-the-captains-room

_ = input ()
l = input ().strip ().split ()
d = dict ()

for i in l:
    if i not in d.keys ():
        d[i] = 0
    d[i] += 1

print (*[n for n in d.keys () if d[n] == 1])
