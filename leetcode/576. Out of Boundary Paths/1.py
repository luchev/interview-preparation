# Complexity (n = matrix rows, k = matrix columns, t = maxMove)
# Time complexity: O(n * k * t)
# Space complexity: O(n * k * t)

class Solution:
    @lru_cache(10000)
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if startRow == m or startColumn == n or startRow < 0 or startColumn < 0:
            return 1
        if maxMove == 0:
            return 0
        return sum(self.findPaths(m, n, maxMove - 1, startRow + drow, startColumn + dcol) for drow,dcol in [(-1,0), (+1,0), (0,-1), (0,+1)]) % (10 ** 9 + 7)