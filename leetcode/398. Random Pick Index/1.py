# Time Limit Exceeded, but interesting idea of calculating
# the random index online
# Complexity(n = input list length)
# Time complexity init: O(1)
# Time complexity pick: O(n)
# Space complexity: O(n)

from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        result = -1
        count = 0
        for i, num in enumerate(self.nums):
            if num == target and random.randint(0, count) == 0:
                result = i
        return result
        
