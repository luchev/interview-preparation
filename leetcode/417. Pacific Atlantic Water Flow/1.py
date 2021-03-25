# Complexity (n = matrix rows, k = matrix columns)
# Time complexity: O(n * m)
# Space complexity: O(n * m)

from typing import List

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        
        nrows = len(matrix)
        ncols = len(matrix[0])
        
        topLeftQ = deque()
        bottomRightQ = deque()
        
        for row in range(nrows):
            topLeftQ.append((row, 0))
            bottomRightQ.append((row, ncols - 1))
            
        for col in range(ncols):
            topLeftQ.append((0, col))
            bottomRightQ.append((nrows - 1, col))
        
        topLeftReachable = bfs(matrix, topLeftQ, nrows, ncols)
        bottomRightReachable = bfs(matrix, bottomRightQ, nrows, ncols)
        
        return topLeftReachable.intersection(bottomRightReachable)
        
def bfs(matrix, frontier, nrows, ncols):
    visited = set()
    while frontier:
        curRow, curCol = frontier.popleft()
        visited.add((curRow, curCol))
        for (drow, dcol) in [(+1,0), (-1,0), (0,+1), (0,-1)]:
            row = curRow + drow
            col = curCol + dcol
            
            if 0 <= row < nrows and 0 <= col < ncols and (row, col) not in visited and matrix[curRow][curCol] <= matrix[row][col]:
                frontier.append((row, col))
        
    return visited
