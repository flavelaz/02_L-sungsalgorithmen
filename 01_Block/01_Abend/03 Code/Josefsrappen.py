jahrstart = float(input("Von welchem Jahr aus möchten Sie starten:"))
jahrende = float(input("Bis zu welchem Jahr möchten Sie wissen: "))
zinssatz = float(input("Zinssatz in %:"))
betrag = float(input("Was ist das Startkapital in CHF"))

kn = betrag * ((zinssatz/100)+1)**(jahrende-jahrstart)
print(kn)

volgold = 0.0000518
volerde = 1087000000000000000000
preisgold = 103571

goldkg = kn/preisgold
volgold2 = volgold*goldkg
voltot = volgold2/volerde

print(voltot)