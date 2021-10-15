from collections import deque, defaultdict
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        return ladderLength(beginWord, endWord, wordList)

# Our solution will be based on BFS.
def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    visitationSet = set()
    wordDict = processWordList(wordList)    # wordList is now a dict indexed by generic words and mapping to actual words from the original wordList.
    queue = deque([])
    queue.append((beginWord, 1))
    visitationSet.add(beginWord)
    while queue:
        word, pathLength = queue.popleft()
        for i in range(len(word)):      # Add all its neighbors from the list.
            if word == endWord:
                return pathLength
            genericWord = word[:i] + '*' + word[(i+1):]
            for neighb in wordDict[genericWord]:
                if neighb not in visitationSet:
                    visitationSet.add(neighb)       # Important to restrict neighbors at this point, since we might be adding them twice in the frontier!
                    queue.append((neighb, pathLength + 1))
    return 0            # If you didn't reach endWord, you didn't return inside the loop.

def processWordList(wordList: List[str]) -> dict:
    retVal = defaultdict(list)      # A subtype of dict that gives us a default value of an empty list whenever we add a key that isn't in the dict already.
    for word in wordList:
        for i in range(len(word)):
            retVal[word[:i] + '*' + word[(i+1):]].append(word)  # Append possible since the key wasn't in the dict, and the defaultdict implementation gives us an empty list.
    return retVal