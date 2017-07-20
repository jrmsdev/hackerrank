#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/append-and-delete

import sys


s = input().strip()
t = input().strip()
k = int(input().strip())

slen = len (s)
tlen = len (t)

nchars = 0
for i in range (tlen):
    tchar = t[i]
    if i < slen:
        schar = s[i]
        if schar == tchar:
            nchars += 1
            continue
        else:
            break

diff = (slen + tlen) - (nchars * 2)

if slen + tlen < k:
    print ("Yes")
elif diff <= k and diff % 2 == k % 2:
    print ("Yes")
else:
    print ("No")
