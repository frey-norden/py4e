#!/usr/bin/env python3
# File: bigups.py
# Use words.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)
for line in fname:
    line = line.rstrip()
    uptxt = line.upper()
    print(uptxt)
