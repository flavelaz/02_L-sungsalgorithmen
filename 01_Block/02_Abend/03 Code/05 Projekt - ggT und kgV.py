zahl1 = int(input("Geben Sie die erste Zahl ein: "))
zahl2 = int(input("Geben sie die zweite Zahl ein: "))

#zahl1 = 48
#zahl2 = 18


#Zwischenspeicher
zahlx1 = zahl1
zahlx2 = zahl2


#ggt Rechnung
while zahl2 != 0:
    zahl1, zahl2 = zahl2, zahl1 % zahl2
print("ggT: ",zahl1)


#kgv Rechnung
kgv = (zahlx1 * zahlx2) // zahl1
print("kgV: ",kgv)

