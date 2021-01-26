# Complexity (n = rows in the matrix, m = cols in the matris, k = max difference between two cells in the matrix)
# Time complexity: O(n * m * log(k))
# Space complexity: O(n * m)

from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        
        def dfs(limit):
            visited = [[False] * cols for _ in range(rows)]
            que = [(0,0)]
            visited[0][0] = True
            while que:
                row, col = que.pop()
                if row == rows - 1 and col == cols - 1:
                    return True
                
                for drow,dcol in [(0,1), (1,0), (0,-1), (-1,0)]:
                    neigh_row = row + drow
                    neigh_col = col + dcol
                    if 0 <= neigh_row < rows and 0 <= neigh_col < cols and not visited[neigh_row][neigh_col]:
                        if abs(heights[row][col] - heights[neigh_row][neigh_col]) <= limit:
                            visited[neigh_row][neigh_col] = True
                            que.append((neigh_row, neigh_col))
                
            return False
        
        left_lim = 0
        right_lim = 10 ** 6
        while left_lim < right_lim:
            mid_lim = (left_lim + right_lim) // 2
            if dfs(mid_lim):
                right_lim = mid_lim
            else:
                left_lim = mid_lim + 1
        
        return left_lim
