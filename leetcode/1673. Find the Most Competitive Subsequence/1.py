# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        
        additional_count = len(nums) - k
        for x in nums:
            while len(stack) > 0 and additional_count > 0 and stack[-1] > x:
                stack.pop()
                additional_count -= 1
            stack.append(x)
        return stack[:k]
