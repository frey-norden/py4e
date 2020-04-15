#!/usr/bin/env python3'
# File: strcomp.py

def strcomp():
    #word = 'ledzeppelin'
    band = input('Enter a band name. ')
    if band == 'ledzeppelin':
        print('cool band')
    #word = 'notzeppelinanymore'
    if band < 'ledzeppelin':
        print('Your band,'+ band + ', comes before ledzeppelin')
    elif band > 'ledzeppelin':
        print('Your band,' + band + ', comes after ledzeppelin')
    else:
        print('All right, cool band, man! Got any ludes?')

def main():
    strcomp()

if __name__ == "__main__":
    main()
