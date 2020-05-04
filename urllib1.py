#!/usr/bin/env python3
# File: urllib1.py

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://localhost:8080/svenska.html')
for line in fhand:
    print(line.decode().strip())
