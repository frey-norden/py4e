#!/usr/bin/env python3
# File: xmlcomments.py

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# ignore ssl cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

sum = 0
i = 0
data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
counts = tree.findall('.//count')
for count in counts:
    num = int(count.text)
    sum += num
    i += 1
print('Count:',i)
print('Sum:',sum)
