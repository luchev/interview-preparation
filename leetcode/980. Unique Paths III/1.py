# Complexity (n = )
# Time complexity: O(n)
# Space complexity: O(3^n)

from typing import List
from typing import Tuple

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        required_path_len = count_grid_visitable(grid)
        start_pos = find_one(grid)
        return traverse(grid, start_pos, 1, required_path_len)

def traverse(grid, current_position, current_path_len, required_path_len) -> int:
    x0, y0 = current_position
    if grid[x0][y0] == 2:
        # print(grid)
        # print(current_path_len, required_path_len)
        if current_path_len == required_path_len:
            return 1
        else:
            return 0
    if grid[x0][y0] < 0:
        return 0
    if grid[x0][y0] > 2:
        return 0
    
    grid[x0][y0] = 7
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    paths = 0
    for d in directions:
        next_position = (x0 + d[0], y0 + d[1])
        if is_position_valid(grid, next_position):
            paths += traverse(grid, next_position, current_path_len + 1, required_path_len)
    
    grid[x0][y0] = 0
    
    return paths
        
def count_grid_visitable(grid: List[List[int]]) -> int:
    visitable = 2
    for row in grid:
        for cell in row:
            if cell == 0:
                visitable += 1
    return visitable

def find_one(grid: List[List[int]]) -> Tuple[int, int]:
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                return (row, col)
    return (-1, -1)

def is_position_valid(grid: List[List[int]], position: Tuple[int, int]) -> bool:
    return position[0] >= 0 and position[0] < len(grid) and position[1] >= 0 and position[1] < len(grid[position[0]])
