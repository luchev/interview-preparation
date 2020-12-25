# Complexity (n = rows in the matrix, m = cols in the matrix)
# Time complexity: O(n * m)
# Space complexity: O(n * m)

from typing import List
from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        if rows > 0:
            cols = len(matrix[0])
        else:
            cols = 0
        diags = defaultdict(list)
        for row in range(rows):
            for col in range(cols):
                diags[row + col].append(matrix[row][col])

        result = []
        for diag in range(rows + cols - 1):
            if diag % 2 == 0:
                result += reversed(diags[diag])
            else:
                result += diags[diag]
        return result
