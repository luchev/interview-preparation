# Complexity (n = number of words, k = total length of all words)
# Time complexity: O(n^2 + k)
# Space complexity: O(n * ALPHABET_SIZE)

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words = list(map(lambda x: (set(x), len(x)), words))
        result = 0
        for i in range(len(words)):
            for k in range(i + 1, len(words)):
                if len(words[i][0].intersection(words[k][0])) == 0:
                    result = max(result, words[i][1] * words[k][1])
        return result