#!/usr/bin/env python3
# File: countinuplines.py

def countthemlines():
    handla = open('somefile.txt')
    counter = 0
    for line in handla:
        counter += 1
    print('Line count:', counter)

def main():
    countthemlines()

if __name__ == "__main__":
    main()
