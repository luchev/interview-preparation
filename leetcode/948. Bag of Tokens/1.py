# Complexity (n = number of tokens)
# Time complexity: O(n*log(n))
# Space complexity: O(1)

from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        max_score = 0
        left = 0
        right = len(tokens) - 1
        while left <= right:
            if tokens[left] > power and score > 0:
                power += tokens[right]
                right -= 1
                score -= 1
            elif tokens[left] <= power:
                power -= tokens[left]
                left += 1
                score += 1
            else:
                break
            max_score = max(max_score, score)
        return max_score
