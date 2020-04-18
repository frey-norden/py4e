#!/usr/bin/env python3
# File: spamcalc.py
def spamcalc():
    count = 0
    spamtotal = 0.0
    fname = input("Enter the spamfile: ")
    fhandla = open(fname)
    for line in fhandla:
        sw = line.startswith('X-DSPAM-Confidence: ')
        if sw:
            zval = line.find('0')
            spval = line[zval:]
            s = float(spval)
            #print(s)
            spamtotal += s
            count += 1
    avg = (spamtotal/count)
    print('Average spam confidence:', avg)

def main():
    spamcalc()

if __name__ == "__main__":
    main()
