noten = [4.5, 5.0, 3.5, 5.5]

a = noten               #Die Variable a refernziert nun auf die liste noten
b = noten.copy()        #b ist eine Kopie von noten

a.append(6.0)           #Bei der Liste a und noten wurde 6.0 hinzugefügt [4.5, 5.0, 3.5, 5.5, 6.0]
b.remove(3.5)           #Bei der kopierten Liste b wurde 3.5 entfernt [4.5, 5.0, 5.5]
b.sort()                #Die Kopierte Liste wurde sortiert [4.5, 5.0, 5.5]

print(noten)            #Ausgabe: [4.5, 5.0, 3.5, 5.5, 6.0]
print(b)                #Ausgabe: [4.5, 5.0, 5.5]

