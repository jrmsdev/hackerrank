#!/usr/bin/env python3

def birthday (s, d, m):
    count = 0
    slen = len (s)
    for i in range (slen - m + 1):
        end = m + i
        if end <= slen:
            c = sum (s[i:end])
            if c == d:
                count += 1
    return count

_ = input ()
arr = list ( map (int, input ().strip ().split ()))
d, m = map (int, input ().strip ().split ())

print (str (birthday (arr, d, m)))
