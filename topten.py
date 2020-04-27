#!/usr/bin/env python3
# File: topten.py

fname = input('Enter a file: ')
fhandla = open(fname)
counts = dict()
for line in fhandla:
    wrdz = line.split()
    for w in wrdz:
        counts[w] = counts.get(w, 0) + 1

lst = list()
for key, val in counts.items() :
    newtup = (val, key)
    lst.append(newtup)
# sort em high to low
lst = sorted(lst, reverse=True)
# ...now for the top ten
for val, key in lst[:10] :
    print(key, val)
