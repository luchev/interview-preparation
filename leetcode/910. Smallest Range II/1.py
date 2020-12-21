# Complexity (n = number of items in the list)
# Time complexity: O(n * log(n))
# Space complexity: O(1)

from typing import List


class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        ans = A[-1] - A[0]
        for i in range(len(A) - 1):
            ans = min(ans, max(A[-1] - K, A[i] + K) -
                      min(A[0] + K, A[i + 1] - K))
        return ans
