#!/usr/bin/env python3

def count_swaps (a):
    sn = 0
    alen = len (a)
    for i in range (alen):
        swap = False
        for j in range (alen - 1):
            k = j + 1
            if a[j] > a[k]:
                a[j], a[k] = a[k], a[j]
                swap = True
                sn += 1
        if not swap:
            break
    print ('Array is sorted in', sn, 'swaps.')
    print ('First Element:', a[0])
    print ('Last Element:', a[alen - 1])

_ = input ()
arr = list (map (int, input ().strip ().split ()))

count_swaps (arr)
