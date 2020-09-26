# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0 or duration == 0:
            return 0

        poisoned = 0
        previousAttack = timeSeries[0]
        for point in timeSeries:
            poisoned += min(duration, point - previousAttack)
            previousAttack = point

        # Address the last point in time and the posion after it
        poisoned += duration

        return poisoned
