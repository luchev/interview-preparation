# Complexity (n = number of items in the list)
# Time complexity: O(n*log(n)) this solution is asympthotically better than the first, but runs slower
# Space complexity: O(1)

from typing import List

class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        left = 0
        right = len(A) - 1
        s = -1
        while left < right:
            if A[left] + A[right] < K:
                s = max(s, A[left] + A[right])
                left += 1
            else:
                right -= 1
        return s
