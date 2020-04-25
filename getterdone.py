#!/usr/bin/env python3
# File: getterdone.py

qty = dict()
names = ['Backus', 'Newell', 'Fibonacci', 'Knuth', 'Fibonacci', 'McCarthy', 'Simon', 'Perlis', 'Fibonacci', 'Putnum', 'Sussman', 'Fibonacci', 'Knuth', 'Turing']

def getterdone():
    for name in names:
        if name in qty:
            x = qty[name]
        else:
            x = 0
        x = qty.get(name, 0)
        print(x)

def settergetter():
    for name in names :
        qty[name] = qty.get(name, 0) + 1
        print(qty)

def main():
    getterdone()
    settergetter()
    getterdone()

if __name__ == "__main__":
    main()
