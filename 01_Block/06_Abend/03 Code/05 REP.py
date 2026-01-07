zahlen = [3,1,3,1,4,3]
gesehen = []

for i in zahlen:
    if i not in gesehen:
        gesehen.append(i)
    else:
        continue
print(gesehen)