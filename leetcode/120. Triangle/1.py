# Complexity (n = triangle rows)
# Time complexity: O(n^2)
# Space complexity: O(n)

from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        currentRow = triangle[0]
        nextRow = []
        for row in triangle[1:]:
            nextRow.append(currentRow[0] + row[0])
            for i in range(1, len(row) - 1):
                nextRow.append(row[i] + min(currentRow[i - 1], currentRow[i]))
            nextRow.append(currentRow[-1] + row[-1])
            
            currentRow = nextRow
            nextRow = []
        
        return min(currentRow)