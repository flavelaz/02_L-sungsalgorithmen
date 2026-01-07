geschlecht = input("Geben Sie Ihr Geschkecht ein: (M/F): ").upper() #Input für das Geschlecht als string
gewicht = float(input("Geben Sie Ihr Gewicht in (kg) ein: ")) #Input für das Gewicht als float

if geschlecht == str("M") or str("m"):
    if gewicht < 55:
        gewichtsklasse = str("Fliegengewicht")
    elif gewicht >= 55 and gewicht < 66:
        gewichtsklasse = str("Leichtgewicht")
    elif gewicht >= 66 and gewicht < 84:
        gewichtsklasse = str("Mittelgewicht")    
    elif gewicht >= 84 and gewicht < 120:
        gewichtsklasse = str("Schwergewicht")
    else:
        gewichtsklasse = str("Zu schwer")

elif geschlecht == str("F") or str("f"):
    if gewicht > 48:
        gewichtsklasse = str("Fliegengewicht")
    elif gewicht >= 48 and gewicht < 55:
        gewichtsklasse = str("Leichtgewicht")
    elif gewicht >= 55 and gewicht < 63:
        gewichtsklasse = str("Mittelgewicht")
    elif gewicht >= 63 and gewicht < 72:
        gewichtsklasse = str("Schwergewicht")
    else:
        gewichtsklasse = str("Zu schwer")

print("Gewichtsklasse: ",gewichtsklasse)