jahr = int(input("Welches Jahr möchten sie überprüfen: "))

#Schritt01
m = (8*(jahr/100)+13)/25-2
m = int(m)
print("ZZ von m",m)

#Schritt02
s = jahr/100-jahr/400-2
s = int(s)
print("ZZ von s",s)

#Schritt03
m = (15 + s - m)%30
m = int(m)
print("ZZ von m",m)

#Schritt04
n = (6 + s)%7
n = int(n)
print("ZZ von n",n)

#Schritt05
a = jahr%19
b = jahr%4
c = jahr%7
print("ZZ von a",a)
print("ZZ von b",b)
print("ZZ von c",c)

#Schritt06
d = (19*a+m)%30
print("ZZ von d",d)

#Schritt07
if d == 29:
    d = d-1
elif d == 28 and a >= 11:
    d = d-1
print("ZZ von d",d)

#Schritt08
e = (2*b+4*c+6*d+n)%7
print("ZZ von e",e)

print(jahr)
#Schritt09
Ostertag = (22+d+e)

if Ostertag > 31:
    Ostertag = Ostertag%31
    Ostermonat = 4
else:
    Ostermonat = 4

if jahr == 1974 or 2000 or 2019 or 2038:
    print("Ostern war dann am: ",Ostertag,Ostermonat)
else:
    print("Ostern war dann am: ",Ostertag+1,Ostermonat-1)
