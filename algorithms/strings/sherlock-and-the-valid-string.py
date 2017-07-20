#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/sherlock-and-valid-string

def isValid(s):
    # Complete this function
    chars = {}
    chars_keys = []
    slen = len (s)
    for i in range (slen):
        c = s[i]
        if c in chars_keys:
            chars[c] += 1
        else:
            chars[c] = 1
            chars_keys.append (c)
    nmap = {}
    nkeys = []
    for c in chars_keys:
        n = chars[c]
        if n not in nkeys:
            nmap[n] = []
            nkeys.append (n)
        nmap[n].append (c)
    if len (nkeys) == 1:
        return "YES"
    elif len (nkeys) > 2:
        return "NO"
    elif len (nmap[nkeys[0]]) != 1 and len (nmap[nkeys[1]]) != 1:
        return "NO"
    return "YES"

s = input().strip()
result = isValid(s)
print(result)
