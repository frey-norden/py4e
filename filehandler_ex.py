#!/usr/bin/env python3
# File: filehandler_ex.py

def handleit():
    xfile = open('somefile.txt')
    for iteratorvar in xfile:
        print(iteratorvar)

def main():
    handleit()

if __name__ == "__main__":
    main()
