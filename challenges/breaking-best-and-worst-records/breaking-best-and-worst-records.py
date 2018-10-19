#!/usr/bin/env python3

def breaking_records (scores):
    rmax = scores[0]
    rmin = scores[0]
    cmax = 0
    cmin = 0
    for n in scores[1:]:
        if n < rmin:
            rmin = n
            cmin += 1
        if n > rmax:
            rmax = n
            cmax += 1
    return (cmax, cmin)

_ = input ()
arr = list (map (int, input ().strip ().split ()))

print (' '.join (map (str, breaking_records (arr))))
