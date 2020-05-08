#!/usr/bin/env python3
# File: jsoncomments.py
# connects with url, pulls json data(nums), and sums tha nums

import urllib.request as UR
import urllib.parse, urllib.error
import ssl, json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter url: ')
    if len(url) < 1 : break
    print('Retrieving', url)
    uh = UR.urlopen(url, context=ctx)

    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    info = json.loads(data)
    count = info["comments"]
    counts = info["comments"][0]['count']
    sum, i = 0, len(count)

    #for k,v in counts:
    for v in range(0,i):
        value = info["comments"][v]['count']
        sum += value

    print('Count:', i)
    print('Sum', sum)
