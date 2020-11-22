# Complexity (n = number of words, k = average length of each word)
# Time complexity: O(n*k)
# Space complexity: O(*kn)

from typing import List
from itertools import reduce

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        word_set = set()
        for word in words:
            word_set.add(reduce(lambda acc, x: acc + x,
                                map(lambda letter: morse[ord(letter) - ord('a')], word)))

        return len(word_set)
