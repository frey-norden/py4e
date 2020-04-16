#!/usr/bin/env python3
# File: newlinestripper.py

def newlinestripper():
    handla = open('somefile.txt')
    for line in handla:
        sline = line.rstrip()
        #if sline.startswith(' bout') :
        print(sline)

def main():
    newlinestripper()

if __name__ == "__main__":
    main()
