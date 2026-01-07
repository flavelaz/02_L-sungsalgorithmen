def aussen():
    x = 10
    def innen():
        print(x) #Innere Funktion kann nur die äusseren Variablen lesen aber nicht verändern
    innen()
