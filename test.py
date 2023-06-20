from itertools import permutations
import enchant
import requests


response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/baasdd")
errorCode = response.json()[0]

for key in errorCode:
    print(key)