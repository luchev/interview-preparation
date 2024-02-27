# Complexity(n = input list length)
# Time complexity init: O(n)
# Time complexity pick: O(1)
# Space complexity: O(n)

from collections import defaultdict
from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.indices = defaultdict(list)
        for index, num in enumerate(nums):
            self.indices[num].append(index)

    def pick(self, target: int) -> int:
        if target not in self.indices:
            return -1
        return random.sample(self.indices[target], 1)[0]
        
