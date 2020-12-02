# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums
