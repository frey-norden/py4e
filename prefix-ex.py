#!/usr/bin/env python3
# File: prefix-ex.py

def find_prefix():
    line = 'Please take off your shoes when you come in the house'
    print(line)
    print('Computer, Does this line start with Please?')
    if (line.startswith('Please')):
        print(True)
    else:
        print(False)
    print('Computer, Does this line start with the letter p?')
    if (line.startswith('p')):
        print(True)
    else:
        print(False)    
def main():
    find_prefix()

if __name__ == "__main__":
    main()
