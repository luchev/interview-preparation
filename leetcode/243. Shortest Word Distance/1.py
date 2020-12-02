# Complexity (n = words in the list, m = average word length)
# Time complexity: O(n * m)
# Space complexity: O(1)

from typing import List
import math

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        shortest = math.inf
        last_index_1 = -math.inf
        last_index_2 = -math.inf
        for index, word in enumerate(words):
            if word == word1:
                last_index_1 = index
            if word == word2:
                last_index_2 = index
            shortest = min(shortest, abs(last_index_1 - last_index_2))

        return shortest
