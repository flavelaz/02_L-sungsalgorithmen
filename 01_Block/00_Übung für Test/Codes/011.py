def zeahle_buchstaben(text): #Definition der Funktion mit dem Name zaehle_buchstaben mit dem Paramater als Platzhalter text
    result = {} #Definition eines leeren dictionary, wird der variable result zugewiesen
    for buchstabe in set(text): #Für element buchstabe in iterierbarem objekt set vom parameter text
        result[buchstabe] = text.count(buchstabe) #setzte im dictionary result an dem key buchstabe die anzahl der summe der buchstaben
    return result # gebe mir das dictionary asu der funktion heraus

wort = "banane"  #der variable wort wird der string banane zugewiesen
print(zeahle_buchstaben(wort)) #aufruf der funtktion zeahle_buchstaben mit dem parameter wort was in diesem beispiel "banane" ist