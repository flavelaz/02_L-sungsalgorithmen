name = "Flavio"
print(f"Hallo {name}!")

print("------------------------------------------")

zahl = 7
for i in range(1, 11):
    produkt = i * zahl
    print(f"{i} x {zahl} = {produkt}")

print("------------------------------------------")

for i in range(1, 11):
    print(f"{i:2} x {zahl:2} = {i*zahl:3}")

print("------------------------------------------")

wert = 3.1415926
print(f"{wert:.2f}")   # → 3.14 (2 Dezimalstellen)
print(f"{wert:.4f}")   # → 3.1416 (4 Dezimalstellen)

print("------------------------------------------")

anteil = 0.256
print(f"{anteil:.1%}")  # → 25.6%

print("------------------------------------------")
