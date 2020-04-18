#!/usr/bin/env python3
# File: filecounter.py
# python implementation of directory file counter

def dircount():
    count = 0

    fname = input('Enter file name: ')
    fhandla = open(fname)
    for line in fhandla:
        count += 1

    print('Total files:', count)

def main():
    dircount()

if __name__ == "__main__":
    main()
