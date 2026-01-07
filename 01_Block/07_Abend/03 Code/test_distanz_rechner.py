def distance_convertor(distanz,variante=0):
    if variante == 0:
        mi_zu_km = distanz * 1.61
        return(mi_zu_km)
    
    elif variante == 1:
        km_zu_mi = distanz / 1.61
        return(km_zu_mi)

    else:
        print("Falscher Variante kann nur 0 oder 1 sein")

def test_distance_convertor():
    assert distance_convertor(1,0) == 1.61                  #Variante 0 testen mi zu km
    assert distance_convertor(1,1) == 0.6211180124223602    #Variante 1 testen km zu mi
    assert distance_convertor(0,0) == 0                     #Variante Grenzwert mit 0
    assert distance_convertor(2,0) == 3.23                  #Variante Falscher test, sollte 3.22 sein


#distanz = int(input("Geben Sie die gewünste Distanz ein "))
#variante = int(input("0 = mi zu km / 1 = km zu mi "))

#print(distance_convertor(distanz,variante))
