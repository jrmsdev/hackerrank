#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/zipped

n, x = map (int, input().strip().split())

total = []
for i in range (x):
    total.append (list (map (float, input ().strip ().split ())))

for u in zip (*total):
    print (sum (u) / x)
