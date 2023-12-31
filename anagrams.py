from itertools import permutations

class anagrams:
    
    def __init__(self, letters):
        self.letters = letters
        self.dictionary = {}
        with open("words.txt") as file:
            for line in file:
                self.dictionary[line.rstrip()] = 0


    def possiblePermutations(self):
        output = []
        for length in range(3, (len(self.letters) + 1)):
            for word in (permutations(self.letters, length)):
                output.append(''.join(word))
        return output


    def possibleWords(self):
        output = []
        for word in self.possiblePermutations():
            if word.upper() in self.dictionary:
                if word not in output:
                    output.append(word)
        return output


    def toString(self):
        print("List of possible words:")
        outputList = [[], [], [], [], []]
        for word in self.possibleWords():
            if len(word) == 7:
                outputList[4].append(word)
            elif len(word) == 6:
                outputList[3].append(word)
            elif len(word) == 5:
                outputList[2].append(word)
            elif len(word) == 4:
                outputList[1].append(word)
            elif len(word) == 3:
                outputList[0].append(word)
        for i in range(7, 2, -1):
            print(f"{i} letter words: ")
            print(outputList[i - 3])


userLetters = anagrams(input("Type the letters: "))
userLetters.toString()