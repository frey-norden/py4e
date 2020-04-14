#!/usr/bin/env python3
# File: ex_05_02.py
# takes a series of numbers from input and returns
# max and min values

max = None
min = None
num = 0
total = 0.0
while True :
    val = input('Enter a number: ')
    if val == 'done' :
        break
    try:
        val = int(val)
    except:
        print('Invalid input')
        continue

    if min is None :
        min = val
    elif val < min :
        min = val
    if max is None :
        max = val
    elif val > max :
        max = val

print('Maximum is', max)
print('Minimum is', min)
