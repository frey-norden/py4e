#!/usr/bin/env python3
# File: urlwords.py

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    wrds = line.decode().split()
    for wrd in wrds:
        counts[wrd] = counts.get(wrd, 0) + 1
print(counts)
