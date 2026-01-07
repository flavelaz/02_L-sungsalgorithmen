import random


tippZahlenList = [] #Leere Liste als Definition


for i in range(6): #Sechs Druchläufe wegen 6 Zahlen.
    zahlTipp = random.randint(1,42)

    while zahlTipp in tippZahlenList:   #Solange zahlTipp in der Liste vorhanden, suche eine neue Zahl
        zahlTipp = random.randint(1,42)
    else:                               #Wenn nicht mehr füge die Zahl in die liste ein
        tippZahlenList.append(zahlTipp)

glücksZahl = random.randint(1,6)

sortierteTippListe = sorted(tippZahlenList)

print("Ihr Lottotipp: ", end=" ")

counter = 0
for i in sortierteTippListe:
    print(sortierteTippListe[counter], end="; ")
    counter += 1

print("Ihre Glückszahl: ", glücksZahl)