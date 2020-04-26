#!/usr/bin/env python3
# File: bigsender.py

fname = input('Enter a file: ')
fhandla = open(fname)
senders = []
counts = dict()
for line in fhandla:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]
    #print(email)
    senders.append(email)
for sender in senders:
    counts[sender] = counts.get(sender, 0) + 1
# now the histogram pattern
bigcount = None
bigsender = None
for email,count in counts.items():
    if bigcount is None or count > bigcount:
        bigsender = email
        bigcount = count
print(bigsender, bigcount)
