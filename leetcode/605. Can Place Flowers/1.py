# Complexity (n = flowerbed size)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List
import math

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        consecutive_zeros = 0
        available_spaces = 0
        has_ones = False
        for x in flowerbed:
            if x == 0:
                consecutive_zeros += 1
            else:
                available_spaces += math.ceil(max(0, consecutive_zeros - 2) / 2)
                consecutive_zeros = 0
                has_ones = True
        available_spaces += math.ceil(max(0, consecutive_zeros - 2) / 2)

        if len(flowerbed) >= 2 and flowerbed[0] == 0 and flowerbed[1] == 0:
            available_spaces += 1
            
        if len(flowerbed) >= 2 and flowerbed[-1] == 0 and flowerbed[-2] == 0:
            available_spaces += 1
        
        if has_ones:
            return available_spaces >= n
        else:
            return math.ceil(len(flowerbed) / 2) >= n
