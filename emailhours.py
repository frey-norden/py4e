#!/usr/bin/env python3
# File: emailhours.py
# find the hour email was sent: create histogram

def findhrs():
    try:
        fname = input('Enter a file ')
        fhandla = open(fname)
    except:
        print('You better not be puttin no SQL inject fool')

    counts = dict()
    for line in fhandla:
        line = line.rstrip()
        if not line.startswith('From '): continue
        wds = line.split()
        hour = wds[5]
        hour = hour[:2]
        #print(hour)
        counts[hour] = counts.get(hour, 0) + 1
    #print(counts)
    lst = list()
    for k,v in counts.items():
        pair = (k,v)
        lst.append(pair)

    lst = sorted(lst)
    #print(lst)
    for k,v in lst:
        print(k,v)

def main():
    findhrs()

if __name__ == "__main__":
    main()
