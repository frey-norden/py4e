#!/usr/bin/env python3
# File: readwholething.py

def readwholething():
    fhandla = open('somefile.txt')
    inp = fhandla.read()
    print(len(inp))

def main():
    readwholething()

if __name__ == "__main__":
    main()
