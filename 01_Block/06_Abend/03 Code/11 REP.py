#Dicionary
noten = {"Anna":[5.0,5.5],"Ben":[4.0],"Clara":[5.5,5.0,5.5]}
"""Anna ist eine Liste mit zwei Noten
Anna ist der Key und die Noten sind die Values"""

for person, werte in noten.items():
#Gib für jede Key die Values aus
    durchschnitt = sum(werte) / len(werte)
    print(person,durchschnitt)