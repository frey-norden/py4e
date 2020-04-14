#!/usr/bin/env python3
# File: pay-calculator.py

hrs = input('Enter hours: ')
rate = input('Enter rate: ')
hrs = float(hrs)
rate = float(rate)


if hrs > 40 :
    othrs = (hrs - 40)
    otrate = (rate * 1.5)
    otpay = othrs * otrate
    grpay = (40 * rate)
    print( grpay + otpay )
else :
    print(hrs * rate)
