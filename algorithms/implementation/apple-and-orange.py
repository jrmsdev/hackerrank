#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/apple-and-orange

import sys

s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

acount = 0
for d in apple:
    p = a + d
    if p >= s and p <= t:
        acount += 1
print (acount)

ocount = 0
for d in orange:
    p = b + d
    if p >= s and p <= t:
        ocount += 1
print (ocount)
