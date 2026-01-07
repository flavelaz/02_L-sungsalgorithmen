woerter = ["Banane", "Kiwi", "Apfel", "Melone"]

sortwoerter = sorted(woerter, key=lambda wort: len(wort))

print(sortwoerter)