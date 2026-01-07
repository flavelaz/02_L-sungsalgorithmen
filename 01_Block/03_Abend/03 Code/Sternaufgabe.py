zeichen = input("Geben Sie ein Zeichen ein: ")
breite = int(input("Breite: "))
höhe = int(input("Höhe: "))

if breite < 2 or höhe < 2:
    print("Error")
    exit()

for i in range(0,höhe,1):
    print(breite * zeichen)

