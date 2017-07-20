#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/py-set-discard-remove-pop

n = int (input ().strip ())
s = set (map (int, input ().strip ().split ()))
N = int (input ().strip ())

for _ in range (N):
    cmd = input ().strip ().split ()
    if cmd[0] == 'pop':
        s.pop ()
    elif cmd[0] == 'remove':
        s.remove (int (cmd[1]))
    elif cmd[0] == 'discard':
        s.discard (int (cmd[1]))

print (sum (s))
