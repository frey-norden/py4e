#!/usr/bin/env python3
# File: sumloop.py

xork = 0
print('Before', xork)
for thing in [9, 41, 12, 3, 74, 15] :
    xork = xork + thing
    print(xork, thing)
print('After', xork)
