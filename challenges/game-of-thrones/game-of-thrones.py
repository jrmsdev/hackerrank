#!/usr/bin/env python3

from sys import stderr
from collections import Counter
from itertools import repeat

def gameOfThrones(s):
    slen = len (s)
    if slen == 1:
        return 'YES'
    if slen == 2:
        if s[0] == s[1]:
            return 'YES'
        else:
            return 'NO'
    oddn = 0
    c = Counter (s)
    for t in c.most_common():
        if t[1] % 2 != 0:
            oddn += 1
        if oddn > 1:
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    s = input()
    print (gameOfThrones(s))
