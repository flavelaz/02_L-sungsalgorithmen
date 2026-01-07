def anwenden(funktion, wert):
    return funktion(wert)

# Tests:

# 1) Lambda, die eine Zahl verdoppelt
print(anwenden(lambda x: x * 2, 5))

# 2) Lambda, die an einen String "!!!" anhängt
print(anwenden(lambda s: s + "!!!", "Hallo"))