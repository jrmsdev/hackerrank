#!/usr/bin/env python3

def hourglass_sum (arr):
    m = None
    for x in range (4):
        for y in range (4):
            s = 0
            h1 = (x, y)
            h2 = (x, y + 1)
            h3 = (x, y + 2)
            h4 = (x + 1, y + 1)
            h5 = (x + 2, y)
            h6 = (x + 2, y + 1)
            h7 = (x + 2, y + 2)
            for c in (h1, h2, h3, h4, h5, h6, h7):
                s += arr[c[0]][c[1]]
            if m is None:
                m = s
            elif s > m:
                m = s
    return m

arr = list ()
for _ in range (6):
    arr.append (list (map (int, input ().strip ().split ())))

print (hourglass_sum (arr))
