#!/usr/bin/env python3
# File: partytime2.py

class PartyAnimal:
    x = 0

    def __init__(self, z):
        self.name = z
        print(self.name,'arrives to party')

    def party(self):
        self.x += 1
        print(self.name, 'party count', self.x)

    def __del__(self):
        print("Party's over", self.x)

sp = PartyAnimal("SeanPaul")
sp.party()

j = PartyAnimal("J_Balvin")
f = PartyAnimal("Farruko")

j.party()
sp.party()
f.party()
