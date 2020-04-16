#!/usr/bin/env python3
# File: inputfilehandla.py

def userpicksfile():
    fname = input('Which file you wanna open: ')
    fhandla = open(fname)
    count = 0
    for line in fhandla:
        if line.startswith('Subject: ') :
            count += 1
    print('There were', count, 'subject lines in', fname)

def main():
    userpicksfile()

if __name__ == "__main__":
    main()
