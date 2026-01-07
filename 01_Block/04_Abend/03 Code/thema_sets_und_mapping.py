"""a = {1,2,3,4,5,6,10}
b = {2,3,4,5,6,7,8,9}

print(a|b) # Vereinigung
print(a&b)  #Schnitt menge
print(a-b) # Differenz
print(a^b)  #Symmetrische Differenz
"""

# Liste mit doppelten Einträgen
namen = ["Brunhilde", "Kunibert", "Brunhilde", "Sieglinde", "Nepomuk", "Ottokar", "Edeltraut", "Sieglinde" ]
# Notenübersicht als Dictionary
noten = {
    "Brunhilde": 5.0,
    "Kunibert": 4.5,
    "Sieglinde": 5.5,
    "Ottokar": 3.5,
    "Edeltraut": 2.5,
    "Bonifacius": 4.0
}


# 01) Doppelte Namen mit Set entfernen → neue Liste 'einzigartig'
einzigartig = list(set(namen))

print("Einzigartige Namen:", einzigartig)

# 02) Prüfen, welche Namen aus 'namen' im Dictionary 'noten' fehlen
for name in einzigartig:
    if name not in noten:
        print(name, "hat keine noten")


# 03) Set aller Vornamen, die in 'noten' vorkommen
vornamen_set = set(noten.keys())
print("Vornamen im Noten-Dictionary:", vornamen_set)

# 04) Durchschnitt aller Noten berechnen
wert = list(noten.values())
durchschnitt = sum(wert)/len(wert)
print("Durchschnittsnote:", round(durchschnitt, 2))


# 05) Lernende mit Note unter 4.0
ungenuegend = []
paare_ungenuegend = []
for name, note in noten.items():
    if note < 4:
		# a) Name und Note ausgeben
        print(name, "Hat eine ungenügende Note", note)
		# b) nur den Namen in Liste 'ungenuegend'
        ungenuegend.append(name)
		# c) (Name, Note) als Tupel in Liste
        paare_ungenuegend.append((name,note))

print("Namen mit Note < 4.0:", ungenuegend)
print("Paare (Name, Note) mit Note < 4.0:", paare_ungenuegend)

python = {"Ottokar", "Bonifacius", "Kunibert", "Edeltraut"}
datenbanken = {"Kunibert", "Bonifacius", "Sieglinde", "Brunhilde"}
# 06) BONUS: Mengenoperationen auf 'python' und 'datenbanken'
schnittmenge = python & datenbanken
vereinigung = python | datenbanken
nur_python  =   python - datenbanken
print("Besuchen beide Module:", schnittmenge)
print("Besuchen mindestens ein Modul:", vereinigung)
print("Besuchen nur Python:", nur_python)
print(type(python))