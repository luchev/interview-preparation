# Complexity (n = number words in the list, k = length of beginWord)
# Time complexity: O(n * k^2)
# Space complexity: O(n * k^2)

# Can be improved with bidirectional bfs

import queue
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # Helps out when constructing Adjacency list
        if beginWord not in wordList:
            wordList.append(beginWord)
        
        # Construct Adjacency list
        edges = {}
        for word in wordList:
            for i in range(len(word)):
                char = word[i]
                wildcard_word = word[:i] + '*' + word[i +1:]
                if wildcard_word not in edges:
                    edges[wildcard_word] = []
                edges[wildcard_word].append(word)
        
        # BFS
        que = queue.Queue()
        que.put((beginWord, 1))
        visited = set()
        while not que.empty():
            word, distance = que.get()
            visited.add(word)
            # We arrived at the desired word
            if word == endWord:
                return distance
            
            # Generate all words with wildcards from the current word
            for i in range(len(word)):
                wildcard_word = word[:i] + '*' + word[i +1:]
                for adj_word in edges[wildcard_word]:
                    if adj_word not in visited:
                        que.put((adj_word, distance + 1))
        return 0
