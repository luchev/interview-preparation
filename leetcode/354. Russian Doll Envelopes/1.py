# Complexity (n = number of envelopes)
# Time complexity: O(n * log(n))
# Space complexity: O(n)

from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        heights = [x[1] for x in envelopes]
        dp = []
        for x in heights:
            pos = bisect_left(dp, x)
            if pos == len(dp):
                dp.append(x)
            else:
                dp[pos] = x
        return len(dp)
