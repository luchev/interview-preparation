# Complexity (n = number of points in the list)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0

        points.sort()
        darts_used = 1
        dart = points[0][1]
        for start, end in points:
            if start <= dart:
                dart = min(dart, end)
            elif dart < start:
                dart = end
                darts_used += 1
        return darts_used
