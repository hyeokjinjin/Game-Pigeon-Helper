import requests
import json

ask = True
while ask == True:
    word = input("Which word should I look up? ")

    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}"

    headers = {
        "X-RapidAPI-Key": "#",
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)


    wordSearch = response.json()
    if wordSearch.get("word"):
        print("TUH")
    else:
        print("NNUHH")
    