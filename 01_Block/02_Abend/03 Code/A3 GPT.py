"""Der Benutzer gibt eine Zahl ein.
Gib mit einer for-Schleife die Multiplikationstabelle (1 × … 10) dieser Zahl aus."""

zahl = int(input("Zahl: "))

for i in range(1,11,1):
    produktwert = i * zahl
    print(i, "x", zahl,"=",produktwert)
