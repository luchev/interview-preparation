# Complexity ()
# Time complexity: O(1)
# Space complexity: O(1)

import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        rounds = minutesToTest // minutesToDie
        return math.ceil(math.log(buckets, rounds + 1))
