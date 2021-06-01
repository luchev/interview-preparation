# Complexity (n = matrix rows, k = matrix columns)
# Time complexity: O(n * k)
# Space complexity: O(n * k)

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                result = max(result, dfs(grid, row, col))

        return result

def dfs(grid: List[List[int]], row: int, col: int) -> int:
    que = [(row, col)]
    squares = 0
    while len(que) > 0:
        row, col = que.pop()
        if grid[row][col] == 0:
            continue
        squares += 1
        grid[row][col] = 0
        for drow, dcol in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
            nextRow = row + drow
            nextCol = col + dcol
            if 0 <= nextRow < len(grid) and 0 <= nextCol < len(grid[row]):
                que.append((nextRow, nextCol))
    
    return squares