#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/alphabet-rangoli

import string

def print_rangoli(size):
    # your code goes here
    L = string.ascii_lowercase
    X = size * 4 - 3
    for i in range (size - 1, 0, -1):
        s = '-'.join (L[i:size])
        print ((s[::-1] + s[1:]).center (X, '-'))
    for i in range (size):
        s = '-'.join (L[i:size])
        print ((s[::-1] + s[1:]).center (X, '-'))


if __name__ == '__main__':
    print_rangoli(int (input ().strip ()))
