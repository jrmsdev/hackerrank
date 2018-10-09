#!/usr/bin/env python3

from collections import Counter

def anagram (s):
	slen = len (s)
	if slen % 2 != 0:
		return -1
	# ~ print ('S:', s, '-', slen)
	mid = int (slen / 2)
	sa = Counter (s[:mid])
	sb = Counter (s[mid:])
	# ~ print ('SA:', sa)
	# ~ print ('SB:', sb)
	count = 0
	for c in sb:
		diff = sb[c] - sa[c]
		# ~ print ('DIFF:', c, '-', diff)
		if diff > 0:
			count += diff
	return count

n = int (input ())
for _ in range (n):
	s = input ()
	print (anagram (s))
