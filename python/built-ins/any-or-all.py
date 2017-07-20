#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/any-or-all

n = int (input ().strip ())
l = input ().strip ().split ()
print (all (int (i) > 0 for i in l) and any (s == s[::-1] for s in l))
