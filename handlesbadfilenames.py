#!/usr/bin/env python3
# File: handlesbadfilenames.py

def fileopener():
    fname = input('Tell me a file name: ')
    try:
        fhandla = open(fname)
    except:
        print('File cannot be opent:', fname)
        quit()

    count = 0
    for line in fhandla:
        if line.startswith('Subject:') :
            count += 1
    print('There were', count, 'subject lines in', fname)

def main():
    fileopener()

if __name__ == "__main__":
    main()
