#!/usr/bin/env python3
# File: findavg.py

def findavg():
    total = 0
    count = 0
    while True :
        inp = input('Enter a number: ')
        if inp == 'done' : break
        value = float(inp)
        total += value
        count += 1

    avg = total / count
    print('Average:', avg)

def main():
    findavg()

if __name__ == '__main__':
    main()
