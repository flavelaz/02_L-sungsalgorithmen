wochenKürzel = input("Wochenkürzel eingeben: ")

while True:
    if wochenKürzel == "MO" or wochenKürzel == "DI" or wochenKürzel == "MI" or wochenKürzel == "DO"  or wochenKürzel == "FR" or wochenKürzel == "SA" or wochenKürzel == "SO":
        print("Gültiger Tag")
        break
    else:
        wochenKürzel = input("Wochenkürzel eingeben: ")
    