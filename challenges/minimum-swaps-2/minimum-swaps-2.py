#!/usr/bin/env python3

def minswap (arr):
    count = 0
    pos = dict ()
    # ~ print ('ARR:', arr)
    for i in range (len (arr)):
        pos[arr[i]] = i
    # ~ print ('POS:', pos)
    xi = 0
    for n in sorted (pos):
        i = pos[n]
        # ~ print ('N:', n, 'XI:', xi, 'I:', i)
        if xi != i:
            pos[arr[i]] = xi
            pos[arr[xi]] = i
            arr[xi], arr[i] = arr[i], arr[xi]
            count += 1
            # ~ print ('ARR:', arr)
            # ~ print ('POS:', pos)
        xi += 1
    return count

_ = input ()
print (minswap (list (map (int, input ().strip ().split ()))))
