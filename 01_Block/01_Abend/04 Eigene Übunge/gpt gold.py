jahrstart = int(input("Von welchem Jahr aus möchten Sie starten: "))
jahrende = int(input("Bis zu welchem Jahr möchten Sie wissen: "))
zinssatz = float(input("Zinssatz in %: "))
betrag = float(input("Startkapital in CHF: "))

# Zinseszins
endkapital = betrag * (1 + zinssatz / 100) ** (jahrende - jahrstart)

# Konstanten
vol_gold_kg = 0.0000518  # m³ pro kg Gold
vol_erde = 1.087e21      # m³ Erde
preis_gold = 103571      # CHF pro kg Gold

# Berechnungen
gold_kg = endkapital / preis_gold
vol_gold_total = vol_gold_kg * gold_kg
anteil_erde = vol_gold_total / vol_erde

# Ausgabe
print(f"\nEndkapital: {endkapital:,.2f} CHF")
print(f"Goldmenge: {gold_kg:,.2f} kg")
print(f"Goldvolumen: {vol_gold_total:.6f} m³")
print(f"Anteil am Erdvolumen: {anteil_erde:.12f}")
