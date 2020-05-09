#!/usr/bin/env python3
# File: juhla3.py
# example of the PartyAnimal class with Finnish variables


class PartyAnimal:
    x = 0
    nimi = " "   # nimi_on ≈ name (en)
    def __init__(self, nimi_on):
        self.nimi = nimi_on
        print(self.nimi, "Juhlan aika")

    def juhla(self):
        self.x += 1
        print(self.nimi, "Kuinka monta juhlaa?", self.x)

class Jaakiekko(PartyAnimal):  # can't remember how to type unicode chars for jääkiekko
    points = 0
    def maali(self):
        self.points += 1
        self.juhla()
        print(self.nimi)

s = PartyAnimal("Saku Koivu")
s.juhla()

t = Jaakiekko("Teemu")
t.juhla()

for m in range(1, 10):
    t.maali()
