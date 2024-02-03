#!/usr/bin/env python3
import pickle
import sys

ladda = input("Vill du ladda tidigare kurs? (j/n): ")
if (ladda == "j"):
    try:
        kurs = pickle.load(open('kurs.p', 'rb'))
    except FileNotFoundError:
        print("Det finns ingen tidigare sparad kurs.")
        kurs = float(input("Ange ny USD-kurs: "))
        pickle.dump(kurs,open('kurs.p', 'wb'))
elif (ladda == "n"):
    kurs = float(input("Ange ny USD-kurs: "))
    pickle.dump(kurs,open('kurs.p', 'wb'))
else:
    sys.exit("Var god svara (j)a eller (n)ej")

usd = float(input("Ange summa i USD: "))
print("%.2f USD motsvarar %.2f SEK" \
    %(usd, usd*kurs))

