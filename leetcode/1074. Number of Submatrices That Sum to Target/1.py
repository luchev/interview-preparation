# Complexity (n = matrix rows, k = matrix cols)
# Time complexity: O(n^2 * k)
# Space complexity: O(n * k)

from typing import List
from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        ps = [[0] * (cols + 1) for _ in range(rows + 1)]
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                ps[row][col] = ps[row - 1][col] + ps[row][col - 1] + matrix[row - 1][col - 1] - ps[row - 1][col - 1]

        result = 0
        for r1 in range(1, rows + 1):
            for r2 in range(r1, rows + 1):
                counts = defaultdict(int)
                counts[0] = 1
                for col in range(1, cols + 1):
                    subsum = ps[r2][col] - ps[r1 - 1][col]
                    result += counts[subsum - target]
                    counts[subsum] += 1
        return result
