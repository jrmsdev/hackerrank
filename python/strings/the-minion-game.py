#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/the-minion-game

def minion_game(s):
    # your code goes here
    vowels = 'AEIOU'
    kevsc = 0
    stusc = 0
    slen = len (s)
    for i in range (slen):
        if s[i] in vowels:
            kevsc += (slen - i)
        else:
            stusc += (slen - i)
    if kevsc > stusc:
        print ("Kevin", kevsc)
    elif kevsc < stusc:
        print ("Stuart", stusc)
    else:
        print ("Draw")


if __name__ == '__main__':
    minion_game(input().strip())
