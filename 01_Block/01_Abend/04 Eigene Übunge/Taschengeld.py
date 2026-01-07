taschengeld = float(input("Wie viel Taschengeld bekommst du in CHF "))
anteil_abgabe = float(input("Wie viel Prozent willst du sparen in Prozent? "))

spar_dezimal = anteil_abgabe/100

spar_monat = taschengeld * spar_dezimal
print("Lea spart jeden Monat",round(spar_monat,2),"CHF")

spar_jahr = spar_monat * 12
print("Lea spart in einem Jahr",round(spar_jahr,2),"CHF")