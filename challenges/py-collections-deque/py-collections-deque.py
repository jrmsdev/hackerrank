#!/usr/bin/env python3

from collections import deque

n = int (input ())
q = deque ()

for _ in range (0, n):
    args = input ().strip (). split (' ')
    cmd = args[0]
    try:
        n = args[1]
    except IndexError:
        pass
    if cmd == 'append':
        q.append (n)
    elif cmd == 'appendleft':
        q.appendleft (n)
    elif cmd == 'pop':
        q.pop ()
    elif cmd == 'popleft':
        q.popleft ()

print (' '.join (q))
