# Complexity (n = number of intervals)
# Time complexity: O(n)
# Space complexity: O(1) excluding the memory for the answer

from typing import List

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        r = toBeRemoved
        new_intervals = []
        for x in intervals:
            if x[1] <= toBeRemoved[0] or toBeRemoved[1] <= x[0]:
                new_intervals.append(x)
            elif toBeRemoved[0] == x[0] and toBeRemoved[1] == x[1]:
                continue
            elif toBeRemoved[0] <= x[0] and toBeRemoved[1] <= x[1]:
                new_intervals.append([toBeRemoved[1], x[1]])
            elif x[0] <= toBeRemoved[0] and x[1] <= toBeRemoved[1]:
                new_intervals.append([x[0], toBeRemoved[0]])
            elif x[0] < toBeRemoved[0] and toBeRemoved[1] < x[1]:
                new_intervals.append([x[0], toBeRemoved[0]])
                new_intervals.append([toBeRemoved[1], x[1]])
        return new_intervals
