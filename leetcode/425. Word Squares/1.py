# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List
from collections import defaultdict

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.prefixes = self.build_prefix_dict(words)
        self.words = words
        self.result = []
        for word in words:
            self.backtrack([word], 1)
        return self.result

    def backtrack(self, square, prefix_index) -> None:
        if len(square) == len(self.words[0]):
            self.result.append(square[:])
            return

        prefix = ''.join([word[prefix_index] for word in square])
        words_with_prefix = self.prefixes[prefix]
        for possible_next_word_index in words_with_prefix:
            possible_next_word = self.words[possible_next_word_index]
            square.append(possible_next_word)
            self.backtrack(square, prefix_index + 1)
            square.pop()

    def build_prefix_dict(self, words: List[str]) -> dict:
        prefix_dict = defaultdict(list)
        for i in range(len(words)):
            word = words[i]
            for prefix_len in range(1, len(word)):
                prefix_dict[word[:prefix_len]].append(i)
        return prefix_dict
