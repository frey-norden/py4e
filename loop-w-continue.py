#!/usr/bin/env python3
# File: loop-w-continue.py

while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')
