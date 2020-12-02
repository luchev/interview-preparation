# Complexity (n = query row)
# Time complexity: O(n^2)
# Space complexity: O(n)

from typing import List

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        cups = [poured] + [0] * query_row
        for row in range(1, query_row + 1):
            for i in range(row, -1, -1):
                cups[i] = max(cups[i] - 1, 0) / 2 + max(cups[i - 1] - 1, 0) / 2
        return min(1, cups[query_glass])
