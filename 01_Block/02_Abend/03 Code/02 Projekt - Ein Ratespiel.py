import random

ranNum = random.randint(1,1)

versuche = 0
maxVersuche = 6
spiel = "J"


while spiel == "J":
    while versuche < maxVersuche:
        guessNum = int(input("An welche Zahl denke ich? "))
        if guessNum == ranNum:
            print("Richtig du hast",versuche,"gebraucht")
            spiel = input("Möchtest du weiter spielen? (J/N)").upper
            versuche = 0 
            break             
        elif guessNum > ranNum:
            print("Meine Zahl ist kleiner!")
            versuche = versuche + 1
        elif guessNum < ranNum:
            print("Meine Zahl ist grösser!")
            versuche = versuche + 1
    else:
        print("Du hast es leider nicht in",versuche, "Versuchen geschafft")
        versuche = 0
        spiel = input("Möchtest du weiter spielen? (J/N)").upper
        break 
else:
    exit()
     
