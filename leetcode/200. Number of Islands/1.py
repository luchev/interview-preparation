# Complexity (n = cells in the grid)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        for i in range(len(grid)):
            grid[i].append('0')
            grid[i].insert(0, '0')
        row = ['0'] * len(grid[0])
        grid.append(row)
        grid.insert(0, row)

        return self.dfs(grid)

    def dfs(self, grid):
        result = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    result += 1
                    stak = [(row, col)]
                    while len(stak) > 0:
                        x, y = stak.pop()
                        if grid[x][y] == '0':
                            continue
                        grid[x][y] = '0'

                        for drow, dcol in [(+1, 0), (-1, 0), (0, +1), (0, -1)]:
                            stak.append((x + drow, y + dcol))

        return result
