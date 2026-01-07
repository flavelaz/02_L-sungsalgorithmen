def produkt(*args):
    ergebnis = 1
    for zahl in args:
        ergebnis = ergebnis * zahl
    return ergebnis
# Tests
print(produkt(2, 3))
print(produkt(2, 3, 4))
print(produkt(2, 3, 4, 5, 6, 7, 8))