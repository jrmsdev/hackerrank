#!/usr/bin/env python3
N = int (input ().strip ())
CL = set ()
for _ in range (N):
    c = input ().strip ()
    CL.add (c)
print (len (CL))
