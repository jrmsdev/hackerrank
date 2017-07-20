#!/usr/bin/env python3


def main (rn, r):

    def rmin (r):
        m = r[0]
        for i in range (1, rn):
            if m == 0 or (r[i] > 0 and r[i] < m):
                m = r[i]
        return m

    def rcut (r, rm):
        ncut = 0
        r2 = []
        for i in range (rn):
            if r[i] >= 1:
                r2.insert (i, r[i] - rm)
                ncut += 1
            else:
                r2.insert (i, 0)
        return (ncut, r2, rmin (r2))

    rm = rmin (r)
    while rm >= 1:
        ncut, r, rm = rcut (r, rm)
        print (ncut)


if __name__ == '__main__':
    from sys import argv
    r = list ()
    idx = -1
    for n in argv:
        if n.isdigit ():
            idx += 1
            r.insert (idx, int (n))
    main (idx + 1, r)
