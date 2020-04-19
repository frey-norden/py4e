#!/usr/bin/env python3
# File: email-list.py

try:
    fname = input('Enter file name: ')
    fhandla = open(fname)
except:
    print('File not found', fname)
count = 0
for line in fhandla:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]
    print(email)
    count += 1
print('There were', count, 'lines in the file with From as the first word')
