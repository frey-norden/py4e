#!/usr/bin/env python3
# File: ex_04_06.py


def computepay():
    hrs = input('Enter hours: ')
    rate = input('Enter rate: ')
    try:
        hrs = float(hrs)
        rate = float(rate)
    except:
        print("Error, please enter numeric input")
        quit()
    if hrs > 40 :
        othrs = (hrs - 40)
        otrate = (rate * 1.5)
        otpay = othrs * otrate
        grpay = (40 * rate)
        ot = grpay + otpay
        return ot
    else :
        st = (hrs * rate)
        return st

p = computepay()
print('Pay',p)
