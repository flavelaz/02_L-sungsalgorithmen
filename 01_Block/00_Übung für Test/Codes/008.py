def auswertung(werte): #Eine Funktion mit dem Namen auswertung wird definiert 
    summe = 0 #Der Summe 0 wird der Wert 0 zugewiesen

    for w in werte: #Für iterierbare Elemente w in iterierbarer Sammlung werte
        if w < 0:   #wenn w kleiner als 0 ist dann: anweisung
            continue #schleifen runde abschliessen und zum nächsten for durchlauf
        summe += w     #Summe mit dem wert der variable w aufsummieren

    if summe >= 20:     #wenn summe grössergleich 20 dann mache:
        status = "ok"   #Variable status wird der wert "ok" zugewiesen
    else:               # wenn if bedingung false dann mache:              
        status = "zu klein" #variable status wird der wert "zu klein" zu gewiesen

    return summe, status #Ausgabewerte aus der funktion summe und status


zahlen = [5, -2, 10, 8]

ergebnis = auswertung(zahlen)

print(ergebnis)

#Der Code fragt eine Liste mit Zahlen ab, in der for schleife summiert er positive zahlen auf und ignoriert die negativen, in der zweiten if schleifeverteilt er den status ok wenn di summer aller positven zahlen grösser 20 ist nost ist der status zu klein. In diesem Fall mit diesen Musterzahlen wäre der status "zu klein"
#werte ist eine Liste
#Summe ist ein Integer
#Status ist ein string
#ergebnis ist ein string
#Augegeben wird: zu klein   <-(die Begründung steht schon in der Zeile 23)