x = 4
y = 7

if x < y:           #Bedingung erfüllt, da 4 < 7
    y = x           # y wird neu 4
elif y == 7:        # elif wird nicht ausgeführt, da der if verglich schon true war
    x = 0

print(x, y)         # x ist imme rnoch 4 und y bekam den wert von x dh auch 4
