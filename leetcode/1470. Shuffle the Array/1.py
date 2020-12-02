# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [x for i in range(n) for x in (nums[i], nums[n + i])]
