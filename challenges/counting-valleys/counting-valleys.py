#!/usr/bin/env python3

def count_valleys (s):
    v = 0
    x = 0
    px = 0
    for c in s:
        if c == 'D':
            x -= 1
        elif c == 'U':
            x += 1
        if x == -1 and px == 0:
            v += 1
        px = x
    return v

_ = input ()
print (count_valleys (input ().strip ()))
