#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/staircase

import sys

n = int(input().strip())

for i in range (n, 0, -1):
    print (' ' * (i - 1), end = '')
    print ('#' * (n - i + 1))
