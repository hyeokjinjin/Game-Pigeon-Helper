import time

class TrieNode:
	def __init__(self):
		self.children = [None]*26
		self.isEndOfWord = False

class Trie:
	def __init__(self):
		self.root = self.getNode()


	def getNode(self):
		return TrieNode()


	def charToIndex(self,ch):
		return ord(ch)-ord('a')


	def insert(self, word):
		trie = self.root
		for letterIndex in range(len(word)):
			index = self.charToIndex(word[letterIndex])

			if not trie.children[index]:
				trie.children[index] = self.getNode()
			trie = trie.children[index]

		trie.isEndOfWord = True


	def search(self, word):
		trie = self.root
		for letterIndex in range(len(word)):
			index = self.charToIndex(word[letterIndex])
			if not trie.children[index]:
				return False
			trie = trie.children[index]
		return trie.isEndOfWord


	def recursionBreak(self, word):
		trie = self.root
		for letterIndex in range(len(word)):
			index = self.charToIndex(word[letterIndex])
			if not trie.children[index]:
				return True
			trie = trie.children[index]
		return False



class wordHunt:
	def recursion(self, row, col, word, visitedBoard):
		if (row < 0 or row >= 4 or col < 0 or col>= 4):
			return
		if (visitedBoard[row][col]):
			return
		if self.t.recursionBreak(word):
			return

		word += self.board[row][col]
		visitedBoard[row][col] = True

		if (len(word) > 2 and (self.t.search(word))):
			self.answer[word] = 0

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
		self.t = Trie()
		with open("words.txt") as file:
			for line in file:
				self.t.insert(line.rstrip().lower())

		self.answer = {}
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

		answerList = self.answer.keys()
		for i in range(len(answerList)):
			print(f"{(i-len(answerList)) * -1}: {sorted(answerList, key=len)[i]}")


wH = wordHunt()
print(f" It took {time.time() - wH.start} seconds to find all solutions")