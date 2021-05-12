# Complexity (n = input matrix rows, m = input matrix columns)
# Time complexity: O(n * m) for precomputing
# Time complexity: O(1) per request
# Space complexity: O(n * m)

from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pre = [[0] * (1 + len(matrix[0])) for _ in range(1 + len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                self.pre[row + 1][col + 1] = self.pre[row][col + 1] + self.pre[row + 1][col] - self.pre[row][col] + matrix[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre[row2 + 1][col2 + 1] - self.pre[row1][col2 + 1] - self.pre[row2 + 1][col1] + self.pre[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)