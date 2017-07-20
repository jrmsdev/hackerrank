#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/py-set-union

_ = input ().strip ()
a = set (map (int, input ().strip ().split ()))
_ = input ().strip ()
b = set (map (int, input ().strip ().split ()))
print (len (a.union (b)))
