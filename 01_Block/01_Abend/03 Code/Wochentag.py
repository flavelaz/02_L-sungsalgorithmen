d = int(input("Tag: "))
m = int(input("Monat: "))
y = int(input("Jahr: "))
compdate = d,m,y

# Aufgabenteil A)
if m <= 2:
    m = m + 10
    y = y - 1
else:
    m = m - 2

# Aufgabenteil B)
c = y // 100
j = y % 100

# Aufgabenteil C)
h = ((26*m - 2)//10 + d + j + j//4 + c//4 - 2*c) % 7 #Fehler in der Formel im Aufgabenblatt -> j + y

# Aufgabenteil D)
if h < 0:
    h = h + 7

# Aufgabenteil E)
if h == 0:
    print("Das Datum", compdate, "war ein Sonntag")
elif h == 1:
    print("Das Datum", compdate, "war ein Montag")
elif h == 2:
    print("Das Datum", compdate, "war ein Dienstag")
elif h == 3:
    print("Das Datum", compdate, "war ein Mittwoch")
elif h == 4:
    print("Das Datum", compdate, "war ein Donnerstag")
elif h == 5:
    print("Das Datum", compdate, "war ein Freitag")
else:
    print("Das Datum", compdate, "war ein Samstag")
