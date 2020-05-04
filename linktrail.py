#!/usr/bin/env python3
# File: linktrail.py

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

names = []
# initial link in linktrail
l = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
for i in range(0,4):
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

    l = links[2]
    print(l)
