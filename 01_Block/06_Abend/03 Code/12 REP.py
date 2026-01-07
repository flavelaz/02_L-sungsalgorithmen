staedte = {"Luzern":25,"Zug":23,"Bern":22}
#Aufgabe 1)
print(staedte.get("Zug"))
#Aufgabe 2)
if staedte.get("Basel") == None:
    print("0")
else:
    print(staedte.get("Basel"))
#Aufgabe 3)
saveValBern = staedte.get("Bern")
staedte.pop("Bern")


#Aufgabe 2) wäre einfach mit: print(staedte.get("Basel", 0))
#Aufgabe 3) besser: saveValBern = staedte.pop("Bern")
