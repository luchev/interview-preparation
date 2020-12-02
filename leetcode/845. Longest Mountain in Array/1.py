# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        climb = 0
        mountain_start = 0
        max_len = 0
        for i in range(1, len(A)):
            if A[i - 1] < A[i]:
                if climb <= 0:
                    climb = 1
                    mountain_start = i - 1
            elif A[i - 1] == A[i]:
                climb = 0
                mountain_start = i
            else:
                if climb == 1 or climb == -1:
                    climb = -1
                    max_len = max(max_len, i - mountain_start + 1)

        return max_len
