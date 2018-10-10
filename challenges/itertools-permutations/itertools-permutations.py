#!/usr/bin/env python3

from itertools import permutations

s, n = input ().strip (). split ()
n = int (n)

for p in permutations (sorted (s), n):
    print (''.join (p))
