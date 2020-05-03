#!/usr/bin/env python3
# File: findsumnum.py

import re

fname = input('Enter a file: ')
fhandla = open(fname)
fh = fhandla
numlist = list()
sum = 0
look = 0
for line in fh:
    line = line.rstrip()
    look = re.findall('[0-9]+', line)
    if len(look) == 0: continue
    print(look)
    for i in range(0,len(look)):
        l = int(look[i])
        numlist.append(l)


print(numlist)

for n in range(0,len(numlist)):
    numlist[n] = int(numlist[n])
    sum += numlist[n]
    print(sum,n)

print(sum)
