# Complexity(n = rows, m = columns)
# Time complexity: O(n * m)
# Space complexity: O(n * m)
# This solution uses DP and memoization to store previous results, hence the additional memory used
# We can improve the DP approach to keep only 1 row/column in memory
# We can use simple recursion and no extra memory but the time complexity would be O(2^(n*m))
# Another solution would be to use combinatorics
class Solution:
    def __init__(self):
        self.paths = dict()

    def uniquePaths(self, n: int, m: int) -> int:
        if n <= 0 or m <= 0:
            return 0
        self.paths = dict()
        return self.calcPaths(1, 1, n, m)

    def calcPaths(self, row, col, rows, cols):
        if row == rows or col == cols:
            return 1
        if (row, col) not in self.paths.keys():
            self.paths[(row, col)] = self.calcPaths(
                row + 1, col, rows, cols) + self.calcPaths(row, col + 1, rows, cols)
        return self.paths[(row, col)]
