# Complexity (n = number of numbers in the list = 4)
# Time complexity: O(1) all permutations are a limited number
# Space complexity: O(1)

import time
import itertools

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        bestTimeFromStr = None
        bestTimeStr = ""
        for permutation in itertools.permutations(A):
            timeStr = "{}{}:{}{}".format(*permutation)
            try:
                timeFromStr = time.strptime(timeStr, '%H:%M')
                if bestTimeStr == "" or timeFromStr > bestTimeFromStr:
                    bestTimeStr = timeStr
                    bestTimeFromStr = timeFromStr
            except:
                pass

        return bestTimeStr
