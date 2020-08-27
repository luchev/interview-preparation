# Complexity (n = number of intervals)
# Time complexity: O(n * log(n))
# Space complexity: O(n)

import bisect
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        result = [-1] * len(intervals)

        start_points = [(x[1][0], x[0]) for x in enumerate(intervals)]
        start_points.sort(key=lambda x: x[0])

        for i in range(len(intervals)):
            pos = bisect.bisect_left(start_points, (intervals[i][1], ))
            if pos < len(start_points):
                result[i] = start_points[pos][1]

        return result
