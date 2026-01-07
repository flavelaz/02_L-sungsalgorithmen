namen = ["Anna","Ben","Anna","Clara"]

namen.append("Tom")
print(namen)

namen.remove("Ben")
print(namen)

namen = set(namen)
namen.discard("Max")
print(namen)