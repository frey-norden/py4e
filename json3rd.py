#!/usr/bin/env python3
# File: json3rd.py

import json
input = '''[
{ "id" : "001",
  "song" : "Keep Grindin",
  "name" : "ESG"
},
{ "id" : "003",
  "song" : "Body Roc",
  "name" : "Fat Pat"
}
]'''

players = json.loads(input)
for player in players:
    print('Baller count:', len(players))
    print('Id', player['id'])
    print('Song -', player['song'])
