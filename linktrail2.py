#!/usr/bin/env python3
# File: linktrail2.py
# chain, chain, chain
# chain of links

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

firstlink = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))
names = []
# initial link in linktrail
l = firstlink
for i in range(0,count):
    #url = input('Enter - ')
    url = l
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    links = []
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        #print(tag.get('href', None))
        link = tag.get('href', None)
        links.append(link)

    l = links[pos-1]
    print(l)
