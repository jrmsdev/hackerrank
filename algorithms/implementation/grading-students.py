#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/grading

import sys

def solve(grades):
    # Complete this function
    r = []
    for n in grades:
        if n < 38 or n % 5 < 3:
            r.append (n)
        else:
            r.append (n + (5 - (n % 5)))
    return r

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
