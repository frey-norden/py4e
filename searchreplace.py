#!/usr/bin/env python3
# File: searchreplace.py
# search a string and replace with new characters

def sreplace():
    try:
        person = input('Enter a name')
    except:
        print('Bad data, man')
        quit
    greet = 'Hello', person
    nstr = greet.replace(person, 'Ricki')
    print(nstr)

def main():
    sreplace()

if __name__ == "__main__":
    main()
