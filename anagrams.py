from itertools import permutations
import enchant


minLen = 3
permutationList = []
userLetters = input("Type the letters: ")
for length in range(minLen, (len(userLetters) + 1)):
    for word in (permutations(userLetters, length)):
        permutationList.append(''.join(word))


outputList = []
d = enchant.Dict("en_US")
for word in permutationList:
    if d.check(word):
        if word not in outputList:
            outputList.append(word)


print("List of possible words:")
for word in reversed(outputList):
    print(word)