import requests
import json

ask = True
while ask == True:
    word = input("Which word should I look up? ")

    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}"

    headers = {
        "X-RapidAPI-Key": "08966acf26msh0533234d53aa5cbp107c40jsn46314c65e6a4",
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    print(response.json())
    wordSearch = response.json()
    if wordSearch.get("word"):
        print("TUH")
    else:
        print("NNUHH")
    