# Complexity (n = number of words, k = max word length)
# Time complexity for init: O(n * k^2)
# Time complexity per query: O(k)
# Space complexity: O(n * k^2)

from typing import List
from collections import defaultdict
Trie = lambda: defaultdict(Trie)
Weight = 'Weight'

class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        
        for weight, word in enumerate(words):
            word += '#'
            for i in range(len(word)):
                ptr = self.trie
                ptr[Weight] = weight
                for k in range(i, 2 * len(word) - 1):
                    ptr = ptr[word[k % len(word)]]
                    ptr[Weight] = weight

    def f(self, prefix: str, suffix: str) -> int:
        ptr = self.trie
        for char in suffix + '#' + prefix:
            if char not in ptr:
                return -1
            ptr = ptr[char]
        return ptr[Weight]


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)