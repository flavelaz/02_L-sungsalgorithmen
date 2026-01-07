"""Lass den Benutzer ein Wort eingeben.
Verwende eine for-Schleife, um die Buchstaben einzeln auszugeben
und am Ende die Anzahl der Buchstaben zu zählen."""


wort = input("Wort: ")
x = 0

for i in wort:
    x += 1
    print("Buchstabe Nr:",x,"=",i)
print("---------------------")
print("Buchstaben Total:",x)
print("---------------------")