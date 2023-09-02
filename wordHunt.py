import time

class wordHunt:

    def recursion(self, row, col, word, visitedBoard):
        if (row < 0 or row >= 4 or col < 0 or col>= 4):
            return
        if (visitedBoard[row][col]):
            return

        word += self.board[row][col]
        visitedBoard[row][col] = True

        if (len(word) > 2 and (word in self.dictionary)):
            self.answer.append(word)

        directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1],
            [1, -1],
            [-1, 1],
            [1, 1],
            [-1, -1]
        ]

        for direction in directions:
            x = direction[0]
            y = direction[1]

            if ((row + x >= 0) and (row + x < 4) and (col + y >= 0) and (col + y < 4)):
                if (not visitedBoard[row + x][col + y]):
                    self.recursion(row + x, col + y, word, visitedBoard)

        visitedBoard[row][col] = False


    def __init__(self):
        self.dictionary = {}
        with open("words.txt") as file:
            for line in file:
                self.dictionary[line.rstrip()] = 0

        self.answer = []
        self.board = []
        for i in range(4):
            letters = input(f"Type the letters of row {i + 1}: ")
            if len(letters) != 4:
                print("Invalid number of letters. Try again.")
                break
            self.board.append(list(letters))

        visitedBoard = [
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False]
        ]
        
        self.start = time.time()
        for i in range(4):
            for j in range(4):
                self.recursion(i, j, "", visitedBoard)





wH = wordHunt()
for word in sorted(wH.answer, key=len):
    print(word)

print(f" It took {time.time() - wH.start} seconds to find all solutions")