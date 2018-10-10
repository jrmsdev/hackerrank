#!/usr/bin/env python3

def jump_clouds (c):
    x = len (c)
    j = 0
    i = 0
    while i < (x - 1):
        if i + 2 < x and c[i + 2] == 0:
                i += 2
                j += 1
        elif i + 1 < x and c[i + 1] == 0:
                i += 1
                j += 1
    return j

_ = input ()
c = list (map (int, input ().strip ().split ()))

print (jump_clouds (c))

