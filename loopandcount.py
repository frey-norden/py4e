#!/usr/bin/env python3
# File: loopandcount.py
# simple loop that iterates through a string and counts
# characters in the str

word = 'ludvigvanbeethoven'
countA = 0
countE = 0
countO = 0
for letter in word :
    if letter == 'a' :
        countA += 1
    if letter == 'e' :
        countE += 1
    if letter == 'o' :
        countO += 1
print('In the word:', word)
print('a:', countA, 'e:', countE, 'o:', countO)
