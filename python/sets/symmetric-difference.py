#!/usr/bin/env python3

M = int (input ().strip ())
a = set (map (int, input ().strip ().split ()))
N = int (input ().strip ())
b = set (map (int, input ().strip ().split ()))

print ('\n'.join (map (str, sorted (a.union (b) - a.intersection (b)))))
