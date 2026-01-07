#Importieren der random Funktion
import random

#Generieren der Zufallszahl
randzahl = random.randint(1,100)


trys = 0 #Versuche auf 0 setzen
inputzahl = 0 #Inputzahl muss definiert sein und auf 0 sein damit die while schlaufe überhaupt startet

while inputzahl != randzahl:
    inputzahl = int(input("An welche Zahl denke ich? "))
    trys += 1

    if inputzahl < randzahl:
        print("Tipp war zu niederig")
    
    elif inputzahl > randzahl:
        print("Tipp war zu hoch")

    elif inputzahl == randzahl:
        print("Richtig! du hast ",trys,"Versuche gebraucht")