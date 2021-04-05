# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        return all(abs(A[i] - i) <= 1 for i in range(len(A)))
