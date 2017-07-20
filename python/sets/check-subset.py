#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/py-check-subset

for i in range(int(input())):
    a = int(input()); A = set(input().split())
    b = int(input()); B = set(input().split())
    print (sorted (A) == sorted (A.intersection (B)))
