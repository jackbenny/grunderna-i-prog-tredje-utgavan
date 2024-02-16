#!/usr/bin/env python3

import signal
import sys

def sigint_hanterare(signal, frame):
    sys.exit("\nDu tryckte på Ctrl-C, hej då...")

signal.signal(signal.SIGINT, sigint_hanterare)

while True:
    svar = input("Skriv något: ")
    print("Du skrev:", str(svar))

