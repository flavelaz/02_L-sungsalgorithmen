"""Schreibe ein Programm, das den Benutzer nach einer Zahl fragt
und dann die Summe aller Zahlen von 1 bis zu dieser Zahl berechnet."""

x = int(input("Geben sie mir eine Zahl ein:" ))
y = 0

for i in range(1,x + 1,1):
    y += i
    #print("i =", i, "→ Zwischensumme =", y)
print("Endergebnis =", y)

