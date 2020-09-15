# Complexity (n = number of items in the list)
# Time complexity: O(n)
# Space complexity: O(n)

import math

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        banned_numbers = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                banned_numbers.add(fronts[i])

        min_good_number = math.inf
        for i in range(len(fronts)):
            if fronts[i] not in banned_numbers and fronts[i] < min_good_number:
                min_good_number = fronts[i]
            if backs[i] not in banned_numbers and backs[i] < min_good_number:
                min_good_number = backs[i]

        if min_good_number != math.inf:
            return min_good_number
        return 0
