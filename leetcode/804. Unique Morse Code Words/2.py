# Complexity (n = number of words, k = average length of each word)
# Time complexity: O(n*k)
# Space complexity: O(*kn)

from typing import List
from itertools import reduce


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_map = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
                     "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        word_set = set(reduce(lambda acc, x: acc + x, map(
            lambda letter: morse_map[ord(letter) - ord('a')], word)) for word in words)

        return len(word_set)
