startZahl = int(input("Startzahl: "))
endZahl = int(input("Endzahl: "))

if endZahl < startZahl or endZahl == startZahl:
    print("!!! Fehler Startzahl ist grösser als Endzahl !!!")
else:
    rounds = endZahl - startZahl
    i = 0
    while i <= rounds:
        print(startZahl+i)
        i = i + 1