#!/usr/bin/env python3
# File: inornotin.py

def inorout():
    somelist = [12, 34, 45, 56, 69]
    print('We have a list in here.')
    print('Let us ask python if some values are in it.')
    print('Is 9 in there?')
    if 9 in somelist:
        print('True')
    else:
        print('not in there')
    print('Is 37 in the list?')
    if 37 in somelist:
        print('True')
    else:
        print('nawh, it aint in there')
    print('Is 45 in the list?')
    if 45 in somelist:
        print('True')
    else:
        print('nawh, it aint in there')
    print('Is 20 in there? If not so, print True')
    if 20 not in somelist:
        print('True')
    else:
        print('ei')
    print('What is the length of the list')
    print("print(len(somelist))")
    print(len(somelist))
    print('What are the contents of the whole list?')
    print("print(somelist)")
    print(somelist)

def main():
    inorout()

if __name__ == '__main__':
    main()
