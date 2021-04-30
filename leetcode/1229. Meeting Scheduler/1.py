# Complexity (n = length of slots1, k = length of slots2)
# Time complexity: O(n * log(n) + k * log(k))
# Space complexity: O(1)

from typing import List

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        
        p1 = 0
        p2 = 0
        while p1 < len(slots1) and p2 < len(slots2):
            left = max(slots1[p1][0], slots2[p2][0])
            right = min(slots1[p1][1], slots2[p2][1])
            if right - left >= duration:
                return[left, left + duration]
            
            if slots1[p1][1] < slots2[p2][1]:
                p1 += 1
            else:
                p2 += 1
            
        return []