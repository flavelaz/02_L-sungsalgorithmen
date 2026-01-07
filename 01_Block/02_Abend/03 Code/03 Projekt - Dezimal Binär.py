decNum = int(input("Geben Sie eine Zahl ein die Sie von Dezimal auf Binär ändern möchten: "))

saveDecNum = str(decNum) #Zwischenspeicher der Eingabe

decList1 = []   #Definition Liste, leere liste damit sie später befüllt werden kann
decList2 = []   #Zwiete Liste aus Spass für eindere befüll Methode

counter = 0

while decNum >= 1:
    i = decNum % 2
    decNum = decNum//2
    decList1.insert(counter,i)  #Variante 1 zum in Liste integrieren
    counter = counter + 1       #Counter wichtig für die erhöhung der Slotplätze der Liste
    decList2.append(i)          #Variante 2 zum in Liste integrieren

decList1.reverse()              #Umkehren der Listenreihenfolge
decList2.reverse()

decText1 = "-".join(str(w) for w in decList1) #Schreiben aller Int-Werte in einen String -> "-" ist der Platzhalter zwischen den Werten
decText2 = "".join(str(w) for w in decList2)

print("Ihre Zahl ",saveDecNum, "Dezimal, enspricht: ")
print(decText1,"Binär")
print(decText2,"Binär")