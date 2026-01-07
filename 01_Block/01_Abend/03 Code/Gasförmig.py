#Alkohol -114, Benzin -45
temp1 = int(input("Geben Sie die Tempereatur ein: ")) #Input wird von Benutzer abgefragt
print("Bei", str(temp1), "Grad ist:")

#Hardcode Gefrierpunkte
gefpWasser = 0
gefpAlkohol = -114
gefpBenzin = -45

#Hardcode Verdampfpunkte
gaspWasser = 100
gaspAlkohol = 78
gaspBenzin = 30

#Abfrage Wasser
if temp1 < gefpWasser: 
    print("Wasser gefrorern")
elif((temp1 >= gefpWasser) and (temp1 < gaspWasser)): 
    print("Wasser flüssig")
elif(temp1 >= gaspWasser):
    print("Wasser ist gasförmig")

#Abfrage Alkohol
if temp1 < gefpAlkohol:
    print("Alkohol ist gefroren")
elif ((temp1>= gefpAlkohol) and (temp1 < gaspAlkohol)):
    print("Alkohol ist flüssig")
elif (temp1 >= gaspAlkohol):
    print("Alkohol ist gasförmig")

#Abfrage Benzin
if temp1 < gefpBenzin:
    print("Benzin ist gefroren")
elif ((temp1>= gefpBenzin) and (temp1 < gaspBenzin)):
    print("Benzin ist flüssig")
elif (temp1 >= gaspBenzin):
    print("Benzin ist gasförmig")