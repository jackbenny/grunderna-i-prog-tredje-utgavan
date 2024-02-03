fil = open("filtest.txt")
print(fil.read())
print("Filens namn:", fil.name)
print("Filens läge:", fil.mode)
print("Är filen stängd?", fil.closed)
fil.close()
print("Är filen stängd?", fil.closed)

