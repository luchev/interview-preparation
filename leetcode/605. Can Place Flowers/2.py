# Complexity (n = flowerbed size)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.append(0)
        
        for i in range(len(flowerbed) - 1):
            if flowerbed[i] == 1:
                continue
            if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0
