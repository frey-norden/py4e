#!/usr/bin/env python3	
# File: grosspay.py
# calculate gross pay from hrs and rate

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
pay = hrs * rate
print("Pay: " + str(pay))
