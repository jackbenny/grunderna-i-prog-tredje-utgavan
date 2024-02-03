#!/usr/bin/env python3

class Husdjur:

    # Skapa grunden och attributen
    def __init__(self, namn, art,
                 farg, laten, atit=0):
        self.namn = namn
        self.art = art
        self.farg = farg
        self.laten = laten
        self.atit = atit

    def gorLjud(self):
        print(str(self.laten + " ") * 3)

    def mata(self):
        print(self.namn, "äter sin mat.")
        self.atit = self.atit + 1
        print(self.namn, "har ätit", self.atit, "gång(er).")

    def __str__(self):
        return ("%s är en %s %s" %
            (self.namn, self.farg, self.art))

class Hund(Husdjur):
    def __init__(self, namn, farg, ras, atit=0):
        Husdjur.__init__(self, namn=namn, farg=farg,
                    atit=atit, art="hund", laten="Voff")
        self.ras = ras

    def vilkenRas(self):
        return (self.namn + " är en " + self.ras)

class Katt(Husdjur):
    def __init__(self, namn, farg, ras, atit=0):
        Husdjur.__init__(self, namn=namn, farg=farg,
                    atit=atit, art="katt", laten="Mjau")
        self.ras = ras

    def vilkenRas(self):
        return (self.namn + " är en " + self.ras)

