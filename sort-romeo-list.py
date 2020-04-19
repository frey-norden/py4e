#!/usr/bin/env python3
# File: sort-romeo-list.py

try:
    fname = input('Enter file name: ')
    fh = open(fname)
except:
    print('File not found', fname)
    quit()

list = []
for line in fh:
    line = line.rstrip()
    l = line.split()
    # you can use this for loop or you can use extend - you choose
    for i in l:
        list.append(i)
    #list.extend(l)
list.sort()

slist = []
for word in list:
    if word not in slist:
        slist.append(word)

print(slist)
