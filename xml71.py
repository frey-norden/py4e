#!/usr/bin/env python3
# File: xml71.py
# this is the first example. I just think xml71 sounds cooler.
# I don't plan to do 71 examples of xml here.

import xml.etree.ElementTree as ET

data = '''
<person>
  <name>D. Bissel</name>
  <phone type="intl">
     +1 202 687 8700
  </phone>
  <email hide="yup"/>
</person>
'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
