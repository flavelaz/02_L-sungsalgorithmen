def sammle_gueltige_eintraege(daten): #Definition der Funktion sammle_gültige_einträge mit dem parameter daten
    gueltige_namen = set() #Der Variable gültige_namen wird ein leeres Set zugewiesen
    index = 0 #Der Varbiable index wird die Zahl 0 zugewiesen

    while index < len(daten): #Solange index kleiner als die länge des paramters ist dann mache:
        name, alter = daten[index] #Weise name udn alter aus der liste daten am wert des index zu.

        if alter >= 18: #wenn alter grössergleich 18 dann mache folgendes
            gueltige_namen.add(name) #Füge dem leeren Set den aktuellen namen hinzu.

        index += 1 #erhöhe den index um 1, beginne wieder am anfang der while schlaufe.

    return gueltige_namen #Rückgabe aus der Funktion ist das Set gültige namen


personen = [ #Diese Liste wird als Parameter unten der Funktion mitgegeben
    ("Anna", 22),
    ("Ben", 17),
    ("Clara", 19),
    ("Ben", 17)
]

ergebnis = sammle_gueltige_eintraege(personen) #Die Rückgabe der Funktion wird auf die Variable Ergebins zugewiesen, die oben definierte Funktion wird augerufen mit dem parameter personen
print(ergebnis) #Die Variable ergebnis wird im terminal ausgegeben
