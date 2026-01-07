jahrip = int(input(" Bitte Jahr eingeben: "))
if jahrip%4 == 0:
    if jahrip%100 != 0:
        if jahrip%400 == 0:
            print("Schaltjahr!")
        else:
            print("Kein Schaltjahr")     
    else:
        print("Kein Schaltjahr")         
else:
    print("Kein Schaltjahr")    