#!/usr/bin/env python3
# File: useappend.py

def useappend():
    liststuff = list()
    print('liststuff = list()')
    liststuff.append('someglasses')
    print("liststuff.append('someglasses')")
    liststuff.append('hockeypuck')
    print("liststuff.append('hockeypuck')")
    print('Now we print out the list')
    print(liststuff)
    print("Yeah?? Now let's add some more stuff in there")
    liststuff.append('teacup')
    print("liststuff.append('teacup')")
    print("print(liststuff)")
    print(liststuff)
    liststuff.append('magic-tophat')
    liststuff.append('rabbit')
    print("liststuff.append('magic-tophat')")
    print("print(liststuff)")
    print(liststuff)
    
def main():
    useappend()

if __name__ == '__main__':
    main()
