#!/usr/bin/env python3
# File: strsplit-ex.py

def examplesplits():
    line = 'A lot                    of spaces'
    print("line = 'A lot                    of spaces'")
    ext = line.split()
    print("ext = line.split()")
    print("print(ext)")
    print(ext)
    print('\n')
    ex1 = 'yhden;toinen;kolmas'
    print("ex1 = 'yhden;toinen;kolmas'")
    esimerkki = ex1.split()
    print("esimerkki = ex1.split()")
    print("print(esimerkki)")
    print(esimerkki)
    print("print(len(esimerkki))")
    print(len(esimerkki))
    print('\n')
    esimerkki = ex1.split(';')
    print("esimerkki = ex1.split(';')")
    print("print(ex1)")
    print(esimerkki)
    print("print(len(esimerkki))")
    print(len(esimerkki))

def main():
    examplesplits()

if __name__ == '__main__':
    main()
