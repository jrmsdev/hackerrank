#!/usr/bin/env python3

from itertools import accumulate

def arrman (n, queries):
    arr = [0 for _ in range (n + 1)]
    # ~ print ('ARR0:', arr)
    for q in queries:
            # ~ print ('Q:', q)
            lo = q[0] - 1
            hi = q[1]
            v = q[2]
            arr[lo] += v
            arr[hi] -= v
    # ~ print ('ARR:', arr)
    return max (accumulate (arr))

n, m = map (int, input ().strip ().split ())
q = list ()

for _ in range (m):
    q.append (list (map (int, input ().strip ().split ())))

print (arrman (n, q))
