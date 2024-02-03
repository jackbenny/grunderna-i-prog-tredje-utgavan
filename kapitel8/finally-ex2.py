#!/usr/bin/env python3
import sys
b = "Hejsan"

try:
    print(b)
except NameError:
    print("'b' finns inte")
    sys.exit("Nu avslutar vi...")
else:
    print("'b' finns visst det")
finally:
    print("Jag exekveras alltid, oavsett vad")

