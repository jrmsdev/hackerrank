#!/usr/bin/env python3

def max_toys (prices, k):
    s = 0
    n = 0
    for p in sorted (prices):
        s += p
        if s <= k:
            n += 1
        else:
            s -= p
    return n

_, k = map (int, input ().strip ().split ())
prices = list (map (int, input ().strip ().split ()))

print (max_toys (prices, k))
