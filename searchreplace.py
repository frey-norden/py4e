#!/usr/bin/env python3
# File: searchreplace.py
# search a string and replace with new characters

def sreplace():
    who = input('Enter a name: ')
    greet = 'Hello person'
    nstr = greet.replace('person', 'Ricki')
    print(nstr)

def main():
    sreplace()

if __name__ == "__main__":
    main()
