# Complexity (n = input array length)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        i = 1
        for i in range(i, len(arr)):
            if arr[i - 1] >= arr[i]:
                break
        
        if i < 2:
            return False
        
        for i in range(i, len(arr)):
            if arr[i - 1] <= arr[i]:
                return False
        
        return True
