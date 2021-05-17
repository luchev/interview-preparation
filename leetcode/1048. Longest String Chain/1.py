# Complexity (n = number of words, k = max word length)
# Time complexity: O(n * log(n) + n * k^2)
# Space complexity: O(n)

from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        graph = defaultdict(int)
        for word in words:
            if len(word) == 1:
                graph[word] = 1
                continue

            for i in range(len(word)):
                shorter = word[:i] + word[i+1:]
                if shorter in graph:
                    graph[word] = max(graph[shorter] + 1, graph[word])

            if word not in graph:
                graph[word] = 1
    
        return max(graph.values())
