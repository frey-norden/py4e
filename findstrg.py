#!/usr/bin/env python3
# File: findstrg.py
# exercise 06_05

def findstrg():
    text = "X-DSPAM-Confidence:    0.8475";
    zeropos = text.find('0')
    print(zeropos)

    #sppos = text.find(' ',zeropos)
    #print(sppos)

    target = text[zeropos:]
    print(float(target))

def main():
    findstrg()

if __name__ == "__main__":
    main()
