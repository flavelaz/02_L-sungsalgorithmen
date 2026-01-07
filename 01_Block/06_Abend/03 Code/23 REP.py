daten = {                   #Daten ist ein Set mit key und values, die keys sind String anna und ben, die values sind listen mit int
    "Anna": [5.0, 5.5],
    "Ben": [4.0, 4.5]
}

def bonus(noten):       #Es wird die Funktion bonus definiert, der die variable noten mitgegeben wird
    kopie = noten.copy()    #von der liste noten wird eine kopie erstellt.... Frage? die liste noten existiert gar nicht ist es dann eine leere Liste???
    for i in range(len(kopie)): # für den index in der spanne on der länge (0) von kopie
        if kopie[i] < 5.0: #wenn der wert am index in der liste kleiner 5.0 ist dann...
            kopie[i] += 0.5 #addiere and diesem index 0.5
    return kopie #wenn die schlaufe durchloffen ist geb die liste kopie zurück

neu = {}   # set neu wird neu defineirt

for name, liste in daten.items(): #Für Name(Key) liste(Value) in daten.items(x,x)
    neu[name] = bonus(liste)

print(daten["Ben"]) #Augabe aus dem Set mit dem Key Ben den Value (Liste mit 4.0 und 4.5)
print(neu["Ben"]) #Neu erstellte Liste durch Bonus mit 0.5 addiert zu den noten
