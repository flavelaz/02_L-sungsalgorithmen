werte = (1, 2, 3, 4)        #Werte ist ein Tupel
liste = list(werte)         #Werte wird von tupel ind eine liste gewandelt

liste[1] = liste[1] * 10    #Es wird auf den Listenplatz 1 zugegriffen und den inhalt mit 10 multipliziert (2*10=20)
liste.append(2)             #Die Zahl 2 wird der Liste am schluss angefügt

s = set(liste)              #Aus der Liste wird ein Set gemacht und auf die Variable s vergeben

print(liste)                #Ausgabe: [1,20,3,4,2]
print(len(s))               #Ausgabe 5
