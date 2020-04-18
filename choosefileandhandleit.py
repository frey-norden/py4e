#!/usr/bin/env python3
# File: choosefileandhandleit.py

def newlinestripper():
    fname = input('Which file you wanna open: ')
    fhandla = open(fname)
    for line in fhandla:
        sline = line.rstrip()
        uptxt = sline.upper()
        print(uptxt)

def main():
    newlinestripper()

if __name__ == "__main__":
    main()
