import string


#inputStr = input("Code eingeben: ")
inputStr = "C<GGJD>CC@DNN@AG<QDJ"

listInputStr = list(inputStr)
print(listInputStr)

sortierteList = sorted(listInputStr)
print(sortierteList)

from collections import Counter
anzahl = Counter(sortierteList)
print(anzahl)

top5 = anzahl.most_common(5)
least5 = anzahl.most_common()[:-6:-1]

print(top5)
print(least5)

firstMost = top5[0][0]
secondMost = top5[1][0]
thirdMost = top5[2][0]
fourthMost = top5[3][0]
fifthMost = top5[4][0]


alphabetList = list(string.ascii_uppercase)

"""indFirst = alphabetList.index(firstMost)
indSecond = alphabetList.index(secondMost)
indThird = alphabetList.index(thirdMost)
indFourth = alphabetList.index(fourthMost)
indFifth = alphabetList.index(fifthMost)"""

if alphabetList.index(firstMost) == True:
    indFirst = alphabetList.index(firstMost)
else:
    indFirst = 0

if alphabetList.index(secondMost) == True:
    indSecond = alphabetList.index(secondMost)
else:
    indSecond = 0

if alphabetList.index(thirdMost) == True:
    indThird = alphabetList.index(thirdMost)
else:
    indThird = 0

if alphabetList.index(fourthMost) == True:
    indFourth = alphabetList.index(fourthMost)
else:
    indFourth = 0

if alphabetList.index(fifthMost) == True:
    indFifth = alphabetList.index(fifthMost)
else:
    indFifth = 0

shiftFirst =    (indFirst - 4)  % 26
shiftSecond =   (indSecond - 4) % 26
shiftThird =    (indThird- 4)   % 26
shiftFourth =   (indFourth- 4)  % 26
shiftFifth =    (indFifth- 4)   % 26

print(shiftFirst,shiftSecond,shiftThird,shiftFourth,shiftFifth)
