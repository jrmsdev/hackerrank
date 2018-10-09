#!/usr/bin/env python3

from collections import Counter

def makingAnagrams (s1, s2):
    c1 = Counter (s1)
    c2 = Counter (s2)
    count = 0
    for c in c2:
        count += abs (c2[c] - c1[c])
        del c1[c]
    for c in c1:
        count += abs (c1[c] - c2[c])
    return count

if __name__ == '__main__':
    s1 = input ()
    s2 = input ()
    print (makingAnagrams (s1, s2))
