#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/python-sort-sort

def sortField (k, L):
    i = 0
    for l in zip (*L):
        if i == k:
            return sorted (l)
        i += 1


def getSorted (k, L, n, m, F):
    s = []
    L2 = L.copy ()
    for i in range (n):
        N = F[i]
        for j in range (n):
            l = L2[j]
            if l is not None:
                if l[k] == N:
                    s.append (L[j])
                    L2[j] = None
                    break
    return s


n, m = input ().strip ().split ()
n, m = [int (n), int (m)]

L = []

for i in range (n):
    l = input ().strip ().split ()
    l2 = []
    for j in range (m):
        l2.insert (j, int (l[j]))
    L.insert (i, l2)

k = int (input ().strip ())

F = sortField (k, L)
for l in getSorted (k, L, n, m, F):
    for n in l:
        print (n, '', end = '')
    print ()
