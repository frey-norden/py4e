#!/usr/bin/env python3
# File: partytime.py

class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x += 1
        print('So far', self.x)

    def __del__(self):
        print('I am destructed', self.x)

ah_yeah = PartyAnimal()
for i in range(0,2):
    ah_yeah.party()

ah_yeah = 33
print('ah_yeah contains', ah_yeah)
