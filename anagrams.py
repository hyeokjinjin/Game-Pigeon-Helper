from itertools import permutations
import enchant
import requests

minLen = 3

posWord = []
letters = input("Type the letters: ")
for length in range(minLen, (len(letters) + 1)):
    for word in (permutations(letters, length)):
        posWord.append(''.join(word))


enchantList = []
d = enchant.Dict("en_US")
for word in posWord:
    if d.check(word):
        if word not in enchantList:
            enchantList.append(word)

print("Enchant List")
for word in reversed(enchantList):
    print(word)

    
#apiList = []
#for word in posWord:
    #response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word)
    #errorCode = response.json()
    #for key in errorCode:
        #print(key)
