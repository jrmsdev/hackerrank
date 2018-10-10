#!/usr/bin/env python3

from collections import Counter

_ = input ()
stock = Counter (input ().strip ().split ())

total = 0
clients = int (input ())
for _ in range (clients):
    size, price = input ().strip ().split ()
    available = stock.get (size, 0)
    if available > 0:
        total += int (price)
        stock[size] -= 1

print (total)
