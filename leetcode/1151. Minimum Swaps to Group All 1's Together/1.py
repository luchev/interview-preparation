# Complexity (n = length of data)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        maxWindow = 0
        window = 0
        for right in range(len(data)):
            window += data[right]
            if right >= ones:
                window -= data[right - ones]
            maxWindow = max(maxWindow, window)
        return ones - maxWindow