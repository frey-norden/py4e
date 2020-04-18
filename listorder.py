#!/usr/bin/env python3
# File: listorder.py
# messin with the list order

def listorder():
    bands = ['Hasse Walli', 'Jimi Hendrix Experience', 'Animals', 'Doors', 'P-Funk', 'Aerosmith', 'The O\'Jays', 'Temptations', 'Lynard Skynard']
    print(bands)
    bands.sort()
    print("bands.sort()")
    print(bands)
def main():
    listorder()

if __name__ == '__main__':
    main()
