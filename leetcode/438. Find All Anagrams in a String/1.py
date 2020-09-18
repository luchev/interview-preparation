# Complexity (n = length of string)
# Time complexity: O(n * ALPHABET_SIZE) in our case the alphabet is of constant size 26
# Space complexity: O(ALPHABET_SIZE)

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pattern = [0] * (ord('z') - ord('a') + 1)
        for char in p:
            pattern[ord(char) - ord('a')] += 1

        anagrams = []
        window = [0] * (ord('z') - ord('a') + 1)
        for index, char in enumerate(s):
            window[ord(char) - ord('a')] += 1

            if index >= len(p):
                window[ord(s[index - len(p)]) - ord('a')] -= 1

            if window == pattern:
                anagrams.append(index - len(p) + 1)

        return anagrams
