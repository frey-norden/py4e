#!/usr/bin/env python3
# File: parse-extract-ex.py

def parse_extract():
    data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
    print('This is the data', data)
    atpos = data.find('@')
    print('In what position is the @ symbol')
    print(atpos)

    sppos = data.find(' ',atpos)
    print(sppos)

    host = data[atpos+1 : sppos]
    print(host)

    pos = data.find('.')
    print(data[pos:pos+3])

def main():
    parse_extract()

if __name__ == "__main__":
    main()
