#!/usr/bin/env python3
# File: findlinestart.py

def findlinestart():
    handla = open('somefile.txt')
    for line in handla:
        sline = line.rstrip()
        if not line.startswith(' bout'):
            continue
        print(sline)
def main():
    findlinestart()

if __name__ == "__main__":
    main()
