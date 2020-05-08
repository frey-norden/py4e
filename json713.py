#!/usr/bin/env python3
# File: json713.py

import json
data = '''{
"name" : "Fat Pat",
"phone" : {
    "type" : "Texas",
    "brand" : "motorola",
    "area code" : "713"
    },
    "ride" : {
        "chrome" : "yes",
        "candy_paint" : "u-know-it!!",
        "leather_seats" : "a-must"
    }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Chrome:', info["ride"]["chrome"])
print('Candy Paint?', info["ride"]["candy_paint"])
