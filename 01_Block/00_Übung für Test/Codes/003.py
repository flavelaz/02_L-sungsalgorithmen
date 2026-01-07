def auswertung_punkte(punkte): #Definition der Funktion mit dem Namen auswertung_punkte mit dem Parameter punkte
    ergebnis = []   #Definition einer leeren Liste, übergabe an die Varible Ergebnis

    for wert in punkte: #Für Wert (Index) im parameter punkte
        if wert >= 5:   #Wenn Wert grössergleich 5 dann
            ergebnis.append("bestanden")    #Hänge in der Liste hintenan den String "Bestanden"
        else: #Sonst
            ergebnis.append("nicht bestanden") #Hänge in der Liste hintenan den String "Nicht Bestanden"

    return tuple(ergebnis) #Sobald fertig mit dem For Loop, rückgabe der listeergebnis aber umgewandelt in ein tuple


noten = [4, 5, 6, 3, 5] #Eine Liste mit 5 elementen wird definiert und auf die variable noten übergeben
resultat = auswertung_punkte(noten) #Die Rückgabe der funktion wird auf die variable resulutat übergeben, die ober definierte funktion wirten mit dem parameter noten ausgeführt

print(resultat) #Die Variable RESULTAT WIRD AUSGEGEBEN