# Complexity (n = number of items in the list)
# Time complexity: O(n * log(n))
# Space complexity: O(1)

from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:K]
