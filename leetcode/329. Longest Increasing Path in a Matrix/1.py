# Complexity (n = matrix rows, k = matrix cols)
# Time complexity: O(n * m)
# Space complexity: O(n * m)

from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        depth = [[-2] * len(matrix[0]) for _ in range(len(matrix))]
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                dfs(matrix, row, col, depth)
        return max(max(row) for row in depth)
                
def dfs(matrix: List[List[int]], row: int, col: int, depth: List[List[int]]):
    if depth[row][col] > -2: # open or visited
        return depth[row][col]
    
    depth[row][col] = -1 # open
    maxChildDepth = 1
    for drow, dcol in [(-1,0), (+1,0), (0,+1), (0,-1)]:
        newRow = row + drow
        newCol = col + dcol
        if 0 <= newRow < len(matrix) and 0 <= newCol < len(matrix[0]) and matrix[row][col] < matrix[newRow][newCol]:
            maxChildDepth = max(maxChildDepth, 1 + dfs(matrix, newRow, newCol, depth))
    
    depth[row][col] = maxChildDepth # close
    return depth[row][col]
