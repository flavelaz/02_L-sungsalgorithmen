num = int(input("Geben Sie eine ganze Zahl ein, bis zu der alle Primzahlen angezeigt werden sollen: "))

for i in range(2, num + 1):  # Schleife von 2 bis zur eingegebenen Zahl
    is_prime = True          # Es wird mal davon ausgegangen, dass es eine Primzahl ist
    for j in range(2, int(i ** 0.5) + 1):  # Nur bis zur Quadratwurzel prüfen
        if i % j == 0:
            is_prime = False    # Falls is = flase dann verlasse die Schleife
            break
    if is_prime:
        print(i) #Gebe die die Primzahl aus
