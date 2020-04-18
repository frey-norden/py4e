#!/bin/usr/env python3
# File: testopener.py

fname = input('Which file you wanna open: ')
fhandla = open(fname)
for line in fhandla:
  sline = line.rstrip()
  uptxt = sline.upper()
  print(uptxt)
