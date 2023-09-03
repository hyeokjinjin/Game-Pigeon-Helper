# Game-Pigeon-Helper
Simple solver for the word games found on GamePigeon 

## What is Word Hunt?
Word Hunt is a game where players are given a 4x4 board of random numbers and have eighty seconds to find as much possible words from the board to earn points. Similar to Anagrams, players are able to earn more points by either more words faster or forming words with longer lengths. The player with the highest points at the end of the time limit wins. 

## How It Works:
- Through the DFS (Depth-first search) algorithm, the script finds all possible combinations of the 4x4 board. Then, the script utilizes a Trie data structure to efficiently and effectively find all real English words within the game board by adding every word in the locally downloaded English dictionary and stopping the recursion when a child node is not found.

### How to Use:
- Type in the 4 letters row by row when prompted and the script will automatically print out all possible combinations of the tiles. 

## What is Anagrams?
Anagrams is a tile-based word game where players have exactly one minute to rearrange letter tiles to form words. Players are able to earn more points by either forming more words faster or forming words with longer lengths. The player with the highest points at the end of sixty seconds wins.  

### How It Works:
- By utilizing the itertools Python module, the permutations function gives all possible permutations of any length with the given letter tiles that the user inputs. Then, the script checks each possible permutation within a locally downloaded English dictionary and outputs only real English words.

### How to Use:
- Type in the 7 or 6 letters given to you and the script will automatically print out all possible combinations of the tiles.
