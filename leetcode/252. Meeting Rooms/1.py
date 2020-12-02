# Complexity (n = number of intervals)
# Time complexity: O(n*log(n))
# Space complexity: O(1)

from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: (x[0], x[1]))
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True
