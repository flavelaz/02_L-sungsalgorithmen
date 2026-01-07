zahlen = [3, 7, 1, 9, 4]
summe = 0

for zahl in zahlen:
    summe += zahl

durchschnitt = summe / len(zahlen)
print("Summe:", summe)
print("Durchschnitt:", durchschnitt)

"""
In der variable zahlen wird eine liste definiert mit 5 werten.
der variable summe wird der wert 0 definiert
solange eine zahl in der liste zahlen ist, addiere mir die zahl der variable dazu.
sobald die schlaufe durchlofen ist errechne mir den durchschnitt, dies geschiet wie folgt, die summe der zahlen soll durch die länge der liste geteilt werden.
danach soll mir der code die summe ausgeben und den durchschnitt
"""