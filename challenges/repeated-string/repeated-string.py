#!/usr/bin/env python3

from collections import Counter

def repeat_string (s, n):
    if s == 'a':
        return n
    slen = len (s)
    rn = n // slen
    remain = n - (slen * rn)
    count = Counter (s)['a'] * rn
    if remain > 0:
        count += Counter (s[:remain])['a']
    return count

s = input ().strip ()
n = int (input ().strip ())

print (repeat_string (s, n))
