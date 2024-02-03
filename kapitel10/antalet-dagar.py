#!/usr/bin/env python3
import datetime

startdatum = input("Ange startdatumet (YYYY-MM-DD): ")
slutdatum = input("Ange slutdatumet (YYYY-MM-DD): ")

datum1 = datetime.datetime.strptime(startdatum, "%Y-%m-%d")
datum2 = datetime.datetime.strptime(slutdatum, "%Y-%m-%d")
skillnad = datum2 - datum1

print("Antalet dagar mellan de angivna datumen är",
    skillnad.days)

