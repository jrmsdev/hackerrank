#!/usr/bin/env python3

def min_bribes (q):
    bribes = 0
    qlen = len (q)
    for i in range (qlen):
        if q[i] - (i + 1) > 2:
            print ('Too chaotic')
            return
    for i in range (qlen):
        swp = False
        for j in range (qlen - 1 - i):
            k = j + 1
            if q[j] > q[k]:
                q[j], q[k] = q[k], q[j]
                swp = True
                bribes += 1
        if not swp:
            break
    print (bribes)

t = int (input ().strip ())
for _ in range (t):
    _ = input ()
    q = list (map (int, input ().strip ().split ()))
    min_bribes (q)
