# Complexity (n = rows of the matrix, k = cols of the matrix)
# Time complexity: O(n + m)
# Space complexity: O(1)

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix) - 1
        col = 0
        
        while row >= 0 and col < len(matrix[0]):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                col += 1
            else:
                row -= 1
        
        return False
