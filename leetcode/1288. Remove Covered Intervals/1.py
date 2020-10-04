# Complexity (n = number of intervals in the list)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x: (x[0], -x[1]))
        last = intervals[0]
        absorbed = 0
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if last[0] <= curr[0] and curr[1] <= last[1]:
                absorbed += 1
            else:
                if last[1] < curr[1]:
                    last = curr

        return len(intervals) - absorbed
