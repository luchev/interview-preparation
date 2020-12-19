# Complexity (n = rows in the grid, m = columns in the grid)
# Time complexity: O(n * m^2)
# Space complexity: O(n * m^2)

from typing import List
import math
from functools import cache

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        @cache
        def dp(row, col1, col2):
            if col1 < 0 or col1 >= cols or col2 < 0 or col2 >= cols:
                return -math.inf

            result = grid[row][col1]
            if col1 != col2:
                result += grid[row][col2]

            if row != rows - 1:
                result += max(dp(row + 1, col1 + shift1, col2 + shift2)
                              for shift1 in [-1, 0, 1]
                              for shift2 in [-1, 0, 1])
            return result

        return dp(0, 0, cols - 1)
