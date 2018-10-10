#!/usr/bin/env python3

from itertools import product

A = map (int, input ().strip ().split ())
B = map (int, input ().strip ().split ())

print (' '.join ([str (t) for t in product (A, B)]))
