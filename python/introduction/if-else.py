#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/py-if-else

if __name__ == '__main__':
    n = int(input())
    r = n % 2
    if r == 0:
        if n > 20 or (n >= 2 and n <= 5):
            print ("Not Weird")
        elif n >= 6 and n <= 20:
            print ("Weird")
    else:
        print ("Weird")
