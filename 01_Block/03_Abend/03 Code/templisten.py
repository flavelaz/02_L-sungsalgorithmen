temperaturen = [18,21,19,22,20,18,17]

#Aufagbe 1)
for i in temperaturen:
    print(i, end="Grad ")

#Aufage 2)
summe = sum(temperaturen)
lenght = len(temperaturen)

ds = summe/lenght
print("\n",round(ds,3))

#Aufageb 3)
temperaturen[1] = 20
print(temperaturen)

#Aufgabe 4)
temperaturen.append(20)
print(temperaturen)

#Aufgabe 5)
print(min(temperaturen),max(temperaturen))