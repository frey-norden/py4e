#!/usr/bin/env python3
# File: str-replace-ex.py

def switcheroo():
    greet = 'Hello Bob'
    nstr = greet.replace('Bob','Jane')
    print(nstr)

    nstr = greet.replace('o', 'X')
    print(nstr)

def main():
    switcheroo()

if __name__ == "__main__":
    main()
