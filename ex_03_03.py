#!/usr/bin/env python3
# File: ex_03_03.py

grade = input("Enter a grade between 0.0 and 1.0 ")
try:
    fg = float(grade)
except:
    print("Error, input out of range")
    quit()

if (fg >= 0.9) & (fg <= 1.0):
    print('A')
elif (fg >= 0.8) & (fg < 0.9):
    print('B')
elif (fg >= 0.7) & (fg < 0.8):
    print('C')
elif (fg >= 0.6) & (fg < 0.7):
    print('D')
elif (fg >= 0.0) & (fg < 0.6):
    print('F')
else:
    print("Error, value out of range")
    quit()
