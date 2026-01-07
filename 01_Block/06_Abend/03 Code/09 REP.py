daten = ("Luzern",[12,14,16],("CH","EU"))

print(daten[1][1])

print(daten[2][1])

listeDaten = list(daten)
listeDaten[0] = "Basel"
tupleDaten = tuple(listeDaten)
print(tupleDaten)