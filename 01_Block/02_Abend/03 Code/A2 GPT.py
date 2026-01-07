"""Lass den Benutzer eine ganze Zahl eingeben.
Gib anschließend alle geraden Zahlen zwischen 1 und dieser Zahl aus."""

zahl = int(input("Zahl: "))

for i in range(2,zahl + 1,2):
    print(i, end=" ")  #end=" " -> macht das Alles neben einander geprinted wird.