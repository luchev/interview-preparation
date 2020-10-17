# Complexity (n = number of words in the list, k = average word lenght)
# Time complexity: O(n*k)
# Space complexity: O(ALPHABET_SIZE)

from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letter_map = {}
        for i in range(len(order)):
            letter_map[order[i]] = i

        for i in range(1, len(words)):
            if not compare_words(words[i - 1], words[i], letter_map):
                return False
        return True


def compare_words(a: str, b: str, letter_map: dict) -> bool:
    for i in range(min(len(a), len(b))):
        if letter_map[a[i]] > letter_map[b[i]]:
            return False
        elif letter_map[a[i]] < letter_map[b[i]]:
            return True
    return len(a) <= len(b)
