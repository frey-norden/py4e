#!/usr/bin/env python3
# File: listslicer.py
# slicin up lists like we do them strings

def listslicer():
    list = [34, 23, 2, 69, 99, 44, 281, 713]
    l = list

    # l[1:3
    # this means up to, but not including, list index 3 - **fyi
    print(l[1:3])

    # l[:4]
    # all of em upto, bni, 4.
    print(l[:4])

    # l[:]
    # now the whole thang
    print(l[:])

def listmethods():
    print('Now we look at some of the list methods')
    print('s = list()')
    s = list()
    print(type(s))
    print('These are the methods in the currently running version of Python3')
    print(dir(s))


def main():
    listslicer()
    listmethods()

if __name__ == '__main__':
    main()
