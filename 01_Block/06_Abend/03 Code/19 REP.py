def filter_gerade_und_quadrat(liste):
    resultat = []                       #Definition der neuen Resultatliste
    for i in liste:
        if i % 2 == 0:                  #Check ob gerade
            resultat.append(i **2)      #Die Zahl quardieren und anhängen
    return resultat                     #Rückgabe sobald fertig mit der forschleife


#testbsp
print(filter_gerade_und_quadrat([1,2,3,4]))