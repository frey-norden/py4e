#!/usr/bin/env python3
# File: bigwordcounter.py

def findbigwordcount():
    fname = input('Enter file name: ')
    fhandla = open(fname)

    qtys = dict()
    for line in fhandla:
        sanat = line.split()
        for sana in sanat:
            qtys[sana] = qtys.get(sana, 0) + 1

    bigcount = None
    bigword = None
    for sana,qty in qtys.items():
        if bigcount is None or qty > bigcount:
            bigword = sana
            bigcount = qty
    print(bigword, bigcount)
    
def main():
    findbigwordcount()

if __name__ == "__main__":
    main()
