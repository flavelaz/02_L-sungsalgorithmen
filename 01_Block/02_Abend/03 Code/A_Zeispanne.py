h = int(input("Geben Sie Stunden ein: "))
m = int(input("Geben Sie Minuten ein: "))
s = int(input("Geben Sie Sekunden ein: "))
print(f"{h}h {m}m {s}s entsprechen")

dezH = h * 1
dezM = m / 60
dezS = s / 3600

print(h)
print(m)
print(s)

print(dezH)
print(dezM)
print(dezS)

dezTotal = float(dezH+dezM+dezS)
print("In dezimaler Form ergibt das: ", dezTotal)