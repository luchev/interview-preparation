# Complexity (n = number of points in the list)
# Time complexity: O(n)
# Space complexity: O(1) excluding the output

from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums:
            return [makeInterval(lower - 1, upper + 1)]
        
        prev = lower - 1
        intervals = []
        for x in nums:
            if prev < x < upper + 1 and x - prev > 1:
                intervals.append(makeInterval(prev, x))
            prev = x
        
        if prev < upper + 1 and upper - prev > 0:
                intervals.append(makeInterval(prev, upper + 1))
            
        return intervals
            
            
def makeInterval(start, end):
    if start + 2 == end:
        return str(start + 1)
    return str(start + 1) + '->' + str(end - 1)
