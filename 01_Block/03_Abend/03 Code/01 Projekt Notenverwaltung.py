notenListe = []
import math

for i in range(6):
    notenInput = float(input("Note eingeben: "))
    if notenInput == -1: ###################################################################Option 1 nach -1 ist die Eingabe fertig
        break
    notenListe.append(notenInput)
    

#Aufgabe a)
summeNoten = sum(notenListe)
lenghtNonten = len(notenListe)

dsNoten = summeNoten/lenghtNonten
print("Ungerundet",dsNoten)
dsNoten10 = round(summeNoten/lenghtNonten,1)
print("Durchschnitt auf zehntel gerundet:", dsNoten10)

#ersteKommaZahl = int((dsNoten*10)%10)
#print("Erste Zahl nach dem Kommma", ersteKommaZahl)

############################################################################################ Option 2
dreiKommaZahl = int(math.floor(dsNoten * 1000)) % 1000
print("Drei Zahlen nach dem Komma", dreiKommaZahl)

if dreiKommaZahl < 225:
    abgerundet = math.floor(dsNoten*2)/2
    print("Abgerundet (x < y.225) auf halbe Note:",abgerundet)

elif dreiKommaZahl >= 225 and  dreiKommaZahl < 500:
    aufgerundet = math.ceil(dsNoten*2)/2
    print("Aufgerundet (x > y.225 und < y.500) auf halbe Note:",aufgerundet)

elif dreiKommaZahl > 500 and dreiKommaZahl < 725:
    abgerundet = math.floor(dsNoten*2)/2
    print("Abgerundet (x > y.500 und < y.725) auf halbe Note:",abgerundet)

elif dreiKommaZahl > 725:
    aufgerundet = math.ceil(dsNoten*2)/2
    print("Aufgerundet (x > y.725) auf halbe Note:",aufgerundet)
    
elif dreiKommaZahl == 500:
    print("Muss nicht gerundet werden: ", dsNoten10)
##############################################################################################    

#Aufagbe b) 
bestNote = max(notenListe)
worstNote = min(notenListe)
print("Die beste Note",max(notenListe),"\nDie schlechteste Note",min(notenListe))

#Aufagbe c)
sortierteListe = sorted(notenListe)
print("Aufsteigende Notenliste", sortierteListe)

#Aufgabe d)
print("Die 3 besten Noten sind: ", sortierteListe[3:])


