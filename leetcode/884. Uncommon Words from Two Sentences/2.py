# Complexity (n = length of A, k = length of B)
# Time complexity: O(n + m)
# Space complexity: O(n + m)

import collections

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        words = collections.Counter(A.split(' ') + B.split(' '))
        return [x for x in words if words[x] == 1]
