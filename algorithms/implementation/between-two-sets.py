#!/usr/bin/env python3

def get_total_x (a, b):
    nmin = max (a)
    nmax = min (b)
    count = 0
    for n in range (nmin, nmax + 1):
        sa = 0
        for x in a:
            sa += n % x
        if sa == 0:
            sb = 0
            for x in b:
                sb += x % n
            if sb == 0:
                count += 1
    return count

_ = input ()
a = list (map (int, input ().strip ().split ()))
b = list (map (int, input ().strip ().split ()))

print (get_total_x (a, b))
