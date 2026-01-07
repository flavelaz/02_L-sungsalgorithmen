listeWT = ["MO","DI","MI","DO","FR","SA","SO"]
inputWT = input("WT: ")
while True:
    if inputWT in listeWT:
        print("Gültiger Tag")
        break
    else:
        inputWT = input("WT: ")