# Complexity (n = number of points in the list)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums:
            return [makeInterval(lower - 1, upper + 1)]
        
        points = [lower - 1]
        for x in nums:
            if points[-1] < x < upper + 1:
                points.append(x)
        
        points.append(upper + 1)
        
        intervals = []
        for i in range(1, len(points)):
            if points[i] - points[i - 1] > 1:
                intervals.append(makeInterval(points[i - 1], points[i]))
            
        return intervals
            
            
def makeInterval(start, end):
    if start + 2 == end:
        return str(start + 1)
    return str(start + 1) + '->' + str(end - 1)
