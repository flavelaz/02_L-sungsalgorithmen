def distance_convertor(distanz,variante=0):
    if variante == 0:
        mi_zu_km = distanz * 1.61
        return(mi_zu_km)
    
    elif variante == 1:
        km_zu_mi = distanz / 1.61
        return(km_zu_mi)

    else:
        print("Falscher Variante kann nur 0 oder 1 sein")

distanz = int(input("Geben Sie die gewünste Distanz ein "))
variante = int(input("0 = mi zu km / 1 = km zu mi "))

print(distance_convertor(distanz,variante))