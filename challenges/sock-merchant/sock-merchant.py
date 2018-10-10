#!/usr/bin/env python3

from collections import Counter

_ = input ()
stock = Counter (input ().strip ().split ())

pairs = 0
for n in stock.values ():
    pairs += int (n / 2)

print (pairs)
