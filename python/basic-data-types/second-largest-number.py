#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

if __name__ == '__main__':
    n = int (input ().strip ())
    arr = list (map (int, input ().strip ().split ()))
    print (sorted (set (arr))[-2])
