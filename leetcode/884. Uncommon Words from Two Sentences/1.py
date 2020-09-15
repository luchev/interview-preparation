# Complexity (n = length of A, k = length of B)
# Time complexity: O(n + m)
# Space complexity: O(n + m)

import collections
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        words = collections.Counter(A.split(' ') + B.split(' '))
        result = []
        for word in words:
            if words[word] == 1:
                result.append(word)
        return result
