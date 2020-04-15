#!/usr/bin/env python3
# File: findstr.py

band = 'ledzeppelin'

def findfunc1():
    pos = band.find('pp')
    print(pos)

def findfunc2():
    aa = band.find('a')
    print(aa)

def main():
    findfunc1()
    findfunc2()

if __name__ == "__main__" :
    main()
