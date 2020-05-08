# fre 8 maj 13:31
# File: geojson2.py

import urllib.request as UR
import urllib.parse as UP, urllib.error
import json, ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    loc = input('Enter location: ')
    if len(loc) < 1: break

    parms = dict()
    parms['address'] = loc
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + UP.urlencode(parms)

    print('Retrieving', url)
    uh = UR.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    #lat = js['results'][0]['geometry']['location']['lat']
    #lng = js['results'][0]['geometry']['location']['lng']
    #print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    pid = js['results'][0]["place_id"]
    print('Place id', pid)
    print('Address', location)
