#!/usr/bin/env python3
# File recursive_fib.py
# adapted from example at: https://www.programiz.com/python-programming/examples/fibonacci-recursion
# recursive function to return Fibonacci sequence


def recurs_fib(n):
    if n <= 1:
        return n
    else:
        return(recurs_fib(n-1) + recurs_fib(n-2))

# need to implement io function here
nterms = int(input('Number of iterations: '))
# need to implement try: except: error handling
if nterms <= 0:
    print('Pls enter positive int')
else:
    print('Fibonacci seq:')
    for i in range(nterms):
        print(recurs_fib(i))
        #want to add this to an list and print the array
