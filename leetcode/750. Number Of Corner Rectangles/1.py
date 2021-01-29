# Complexity (r = rows, c = cols)
# Time complexity: O(r * c^2)
# Space complexity: O(c^2)

from typing import List
from collections import defaultdict

class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        if len(grid) <= 1:
            return 0
        
        accumulator = defaultdict(int)
        
        counter = 0
        for row in grid:
            for i in range(0, len(row)):
                for k in range(i + 1, len(row)):
                    if row[i] == 1 and row[k] == 1:
                        counter += accumulator[(i,k)]
                        accumulator[(i,k)] += 1
        return counter
