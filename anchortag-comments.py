#!/usr/bin/env python3
# File: anchortag-comments.py

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# ignore them cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

comments = []
total = 0
num = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # look @ the parts of the tag
    #print('TAG:', tag)
    #print('Contents:', tag.contents[0])
    commentnum = tag.contents[0]
    commentnum = int(commentnum)
    comments.append(commentnum)
    total += commentnum
    num += 1
print(num,total)
#print(comments)
