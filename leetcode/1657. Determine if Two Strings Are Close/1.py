# Complexity (n = length of word 1, m = length of word2)
# Time complexity: O(n + m)
# Space complexity: O(ALPHABET_SIZE)

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        return set(counter1.values()) == set(counter2.values()) \
            and set(counter1.keys()) == set(counter2.keys())
