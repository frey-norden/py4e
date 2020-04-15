#!/usr/bin/env python3
# File: space-strip-ex.py
# stripping whitespace from around words
def tidyup_whitespace():
    tidy = '       Well I always like to tidy up sentences      '
    print(tidy)
    leftside = tidy.lstrip()
    print(leftside)
    rightside = tidy.rstrip()
    print(rightside)
    bothsides = tidy.strip()
    print(bothsides)
def main():
    tidyup_whitespace()

if __name__ == "__main__":
    main()
