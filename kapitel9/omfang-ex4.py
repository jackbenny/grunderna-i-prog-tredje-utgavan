#!/usr/bin/env python3

var = "Lisa"

def funk1():
    global var
    var = "Kalle"
    return var

print("Inifrån funk1 är 'var':", funk1())
print("Globalt är 'var':", var)

