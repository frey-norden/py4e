#!/usr/bin/env python3
# File: upstr.py
# makes str all uppercase

def upstr():
    try:
        band = input('Enter a band, man: ')
    except:
        'Bad data, man'
        quit()

    strup = band.upper()
    print(strup, 'is the best, man!')

def main():
    upstr()

if __name__ == "__main__":
    main()
