eingabe = 0
summe = 0

while True:
    eingabe =int(input("Geben Sie eine Zahl ein: / Mit der Zahl 0 brechen Sie ab!"))
    if eingabe < 0:
        continue
    elif eingabe > 0:
        summe += eingabe
    elif eingabe == 0:
        break
print(summe)
