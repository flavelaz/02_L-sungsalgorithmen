namesee = str(input("Eingabe Name des Sees: "))
volumeninput = int(input("Eingabe Volumen in m^3des Sees: "))
gewichtinput = float(input("Durchschnitt Gewicht der Menschen in kg: "))

if volumeninput <=0 or gewichtinput <= 0:
    print(" Eingabe zu klein, keine Eingaben unter 0 erlaubt")
    exit() 


volperson = ((0.7)*gewichtinput)/1000
weltbev = 8244000000


#Gesamt Vol Menschen
gesamtvolmensch = volperson*weltbev
print("Gesamtvolumen aller Menschen:", gesamtvolmensch)


#Prozentualer Anteil am Seevolumen
prozentvolamsee = (gesamtvolmensch/volumeninput)*100
print("Der Prozentualeanteil im Verhältins zu See und Menschen ist: ",prozentvolamsee)

if prozentvolamsee < 100:
    print("Ja die ganze Menschheit hat platz im", namesee,"wenn alle Menschen ",gewichtinput,"kg sind.")
else:
    print("Nein es haben nicht alle Menschen in diesem See platz")

