"""Der Benutzer gibt eine Zahl ein.
Gib anschließend ein Dreieck aus Sternen * aus, z. B.:

*
**
***
****
*****
    
"""

zahl = int(input("Zahl eingeben: "))
flocke = "*"

for i in range(1,zahl + 1,1):
    print(i * flocke)
