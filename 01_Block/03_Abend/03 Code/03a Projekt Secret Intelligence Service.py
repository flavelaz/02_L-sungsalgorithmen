import string
alphabetList = list(string.ascii_uppercase)


"""
Beispiele
Verschlüsseln: Hallo World / Versatz 5
Entschlüsseln: C<GGJRJMG? / Versatz -5
"""


inputSatz = input("Geben Sie ihre Nachricht ein: ")
inputVerschiebung = int(input("Geben Sie die Gewünschte Verschiebung ein: "))

listeInputSatz = list(inputSatz)
listeInputSatz = [x for x in listeInputSatz if x.strip() != ""] #<--------- Eliminiert alle Leerschläge
satzLänge = len(listeInputSatz)

listeAlphbetPosition = []
listeAlphabetPositionVerschoben = []
listeVerschlüsselt = []

counter = 0
for i in range(satzLänge):
    buchstabe = listeInputSatz[counter]
    counter += 1
    position = ord(buchstabe.upper()) - ord('A') + 1
    listeAlphbetPosition.append(position)
#print("Satz als ABC Position", listeAlphbetPosition)

counter = 0
for i in range(satzLänge):
    buchstabe = listeInputSatz[counter]
    counter += 1
    position = ord(buchstabe.upper()) - ord('A') +1 +inputVerschiebung
    listeAlphabetPositionVerschoben.append(position)
#print("Versetzte ABC Position", listeAlphabetPositionVerschoben)

counter = 0
for i in range(satzLänge):
    zahl = listeAlphbetPosition[counter]
    counter += 1
    buchstabe = chr(zahl + ord('A') -1 -inputVerschiebung)
    listeVerschlüsselt.append(buchstabe)
#print("Versetzter Satz",listeVerschlüsselt)
strOutput = "".join(listeVerschlüsselt)
print("Die entschlüsselte oder verschlüsselte Nachricht: ",strOutput)