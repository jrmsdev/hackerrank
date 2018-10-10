#!/usr/bin/env python3

# ~ https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/

# ~ Input
 # ~ 1  2  3
 # ~ 4  5  6
 # ~ 7  8  9

# ~ Output:
 # ~ 3  6  9
 # ~ 2  5  8
 # ~ 1  4  7

# ~ Input:
 # ~ 1  2  3  4
 # ~ 5  6  7  8
 # ~ 9 10 11 12
# ~ 13 14 15 16

# ~ Output:
 # ~ 4  8 12 16
 # ~ 3  7 11 15
 # ~ 2  6 10 14
 # ~ 1  5  9 13

i0 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for arr in (i0, ):
    maxidx = len (arr) - 1
    for x in range (maxidx, -1, -1):
        l = list ()
        for y in range (0, maxidx + 1):
            l.append (arr[y][x])
        print (*l)
