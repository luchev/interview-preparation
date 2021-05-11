# Complexity (n = number of cards)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints[-k:])
        best = total
        for i in range(k):
            total += cardPoints[i]
            total -= cardPoints[-k + i]
            best = max(best, total)
        return best